# beginners_sat_openCV
Beginners guide to interactive manipulation of satellite data with open cv

https://www.linkedin.com/pulse/beginners-guide-user-interaction-opencv-python-satellite-andrew-cutts

![alt tag](http://www.acgeospatial.co.uk/wp-content/uploads/2017/06/Title.png)


Beginners guide to user Interaction with OpenCV in Python
Posted on 18th June 2017

I have been working with OpenCV for a while now and I still find the speed of results very impressive. It makes for a compelling case for its use in image processing. Computer Vision, at least to me, represents such an incredible opportunity for Remote Sensing specialists as well as non-specialists. I have been meaning to write a beginners guide for a while now and basing it around user interaction seems to be an excellent introduction to OpenCV.
Installing OpenCV

You are going to need Python (either Python 3 or Python 2.7) installed on your computer. I generally use Python 2.7 and OpenCV 3.2. Here is a guide to installing OpenCV on windows; have patience it’s worth it!

http://docs.opencv.org/3.2.0/d5/de5/tutorial_py_setup_in_windows.html

If you are successful, calling import cv2 from a Python GUI should return no errors.

Start by opening an image and viewing it

import cv2
img = cv2.imread('yourimage.jpg')
cv2.imshow('original', img)
cv2.waitKey(0)
cv2.destroyAllWindows


Beginners guide to user Interaction with OpenCV in Python
Posted on 18th June 2017

I have been working with OpenCV for a while now and I still find the speed of results very impressive. It makes for a compelling case for its use in image processing. Computer Vision, at least to me, represents such an incredible opportunity for Remote Sensing specialists as well as non-specialists. I have been meaning to write a beginners guide for a while now and basing it around user interaction seems to be an excellent introduction to OpenCV.
Installing OpenCV

You are going to need Python (either Python 3 or Python 2.7) installed on your computer. I generally use Python 2.7 and OpenCV 3.2. Here is a guide to installing OpenCV on windows; have patience it’s worth it!

http://docs.opencv.org/3.2.0/d5/de5/tutorial_py_setup_in_windows.html

If you are successful, calling import cv2 from a Python GUI should return no errors.

Start by opening an image and viewing it

import cv2
img = cv2.imread('yourimage.jpg')
cv2.imshow('original', img)
cv2.waitKey(0)
cv2.destroyAllWindows

This should be enough to view the image… save the file as xxx.py and run it. For this example I am using a clipped Sentinel2 image of Iran. If I have lost you and you don’t know how to run a Python script this is an excellent guide.

![alt tag](http://www.acgeospatial.co.uk/wp-content/uploads/2017/06/sentinel2-768x481.jpg)
