import cv2
import numpy as np

### this script will open a new window and display the colour that has been click on in the image

def click_event(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		## get the colour
		red = img[y,x,2]
		blue = img[y,x,0]
		green = img[y,x,1]
		## plot the point clicked
		cv2.circle(img,(x,y), 3, (0,0,255), -1)	
		## create a new image called colour_image	
		colour_image = np.zeros((300,500,3), np.uint8)
		## set the colour
		colour_image[:] = [blue,green,red]
		## display the colour image
		cv2.imshow('colour', colour_image)	
			
img = cv2.imread('..//image.jpg')
clone = img.copy()
cv2.imshow('original', img)


cv2.setMouseCallback("original", click_event)
cv2.waitKey(0)

cv2.destroyAllWindows
