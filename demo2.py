### Script to draw a point on each click and connect a line on an (satellite) image using opencv
import cv2
import numpy as np

def click_event(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		### Place a point on the location of click
		cv2.circle(img,(x,y), 3, (0,0,255), -1)	
		point.append((x,y))
		### draw a line on the image once we have 2 or more points in point list
		if len(point) >= 2:
			cv2.line(img,point[-1],point[-2],(0,0,0),2)	
		cv2.imshow('original', img)
				
img = cv2.imread('../image.jpg')
cv2.imshow('original', img)
point = []
cv2.setMouseCallback("original", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows
