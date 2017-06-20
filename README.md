# beginners_sat_openCV
Beginners guide to interactive manipulation of satellite data with open cv

[demo1.py](https://github.com/acgeospatial/beginners_sat_openCV/blob/master/demo1.py) - script to display image and right and left click to display information about colours / row & column

[demo2.py](https://github.com/acgeospatial/beginners_sat_openCV/blob/master/demo2.py) - script to plot a point (in red) on image and draw a line (in black) between points

read below for blog post from 18th June 2017

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

By pressing escape you will close all windows, or in this case the image window.

Create an event handler

Don’t be put off, this is much simpler than you may think. First, build a function to do something when the mouse is clicked. Let’s return the x,y (rows, columns) of the image.

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print x, y
        
You have to parse the 5 arguments (event, x, y, flags, param) for opencv to recognise the event (line 1). Line 2 says if the event is a left mouse click then print to the terminal x and y (line 3). Add this to the top of the script (just after the import cv2 line).

Finally add this line between lines “cv2.imshow(‘original’, img)” and “cv2.waitKey(0)”

cv2.setMouseCallback("original", click_event)

Check the cmd prompt: you should see x,y printed.

Finally let’s print the RGB values onto the image after a right mouse click

Add this code to the def click_event

if event == cv2.EVENT_RBUTTONDOWN:
        red = img[y,x,2]
        blue = img[y,x,0]
        green = img[y,x,1]
        print red, green, blue ### prints to command line
        strRGB = str(red) + "," + str(green) + "," +str(blue)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,strRGB,(x,y), font, 1,(255,255,255),2)
        cv2.imshow('original', img)

What is happening here? In lines 2,3&4 we are getting the red, green and blue values from the image. I have ordered them in RGB, but notice the values in the square brackets – the 3rd value is the colour value (OpenCV works in BGR colour space hence the ordering). Line 4 prints the values to the cmd prompt, line 5 creates a string out of these values, eg “255,0,255” – this is assigned to the variable strRGB. Line 6 assigns the font to use and line 7 is where text is assigned.

I will try and make a bit more sense of line 8: cv2.putText takes 7 arguments above but what do these mean?

img – this is the image we are working with

strRGB – this is the text we want to print

(x,y) – this is the location we are going to put the text

font – this is the image font; we assigned it in line 6, above

1 – this is the scale factor, we are setting it to 1 in this case

(255,255,255) – this is the colour of the text, in this case white

2 – this is the text thickness.

I hope that is clear. If not, have a look at the official documentation.

If you run all this code then hopefully when you right click the RGB values will start to appear on the screen.

![alt tag](http://www.acgeospatial.co.uk/wp-content/uploads/2017/06/Title.png)

