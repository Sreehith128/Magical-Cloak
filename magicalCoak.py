import cv2
import numpy as np 

def empty(a):
	pass

cv2.namedWindow('HSV')
cv2.resizeWindow('HSV',640,320)
cv2.createTrackbar('hMin',"HSV",85,179,empty)
cv2.createTrackbar('hMax',"HSV",145,179,empty)
cv2.createTrackbar('sMin',"HSV",255,255,empty)
cv2.createTrackbar('sMax',"HSV",255,255,empty)
cv2.createTrackbar('vMin',"HSV",0,255,empty)
cv2.createTrackbar('vMax',"HSV",127,255,empty)

def ColorFilter(img):
	imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	imgHSV=cv2.GaussianBlur(imgHSV,(5,5),0)
	hMin=cv2.getTrackbarPos('hMin','HSV')
	hMax=cv2.getTrackbarPos('hMax','HSV')
	sMin=cv2.getTrackbarPos('sMin','HSV')
	sMax=cv2.getTrackbarPos('sMax','HSV')
	vMin=cv2.getTrackbarPos('vMin','HSV')
	vMax=cv2.getTrackbarPos('vMax','HSV')
	mask=cv2.inRange(imgHSV,np.array([hMin,sMin,vMin]),np.array([hMax,sMax,vMax]))
	return mask

bg=cv2.imread('bg.jpg')
cam=cv2.VideoCapture(0)


while True:
	_,frame=cam.read()

	mask=ColorFilter(frame)
	mask1=cv2.morphologyEx(mask,cv2.MORPH_OPEN,np.ones((5,5),np.uint8))
	behind=cv2.bitwise_and(bg,bg,mask=mask)
	live=cv2.bitwise_and(frame,frame,mask=cv2.bitwise_not(mask))
	cloak=cv2.add(behind,live)
	cv2.imshow('Magical Cloak',cloak)
	if cv2.waitKey(1) & 0xff == ord('q'):
		break
cam.release()
cv2.destroyAllWindows()