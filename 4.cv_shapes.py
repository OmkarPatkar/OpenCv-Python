import numpy as np
import cv2

#img = cv2.imread('lena.jpg', 1)

#create img using numpy zeros method
img = np.zeros([512, 512, 3], np.uint8)

#draw a line...(255(b), 0(g), 0(r))
img = cv2.line(img, (0,0), (255,255), (255, 0, 0), 5)

#draw an arrow
img = cv2.arrowedLine(img, (0,255), (255,255), (0, 255, 0), 10)

#draw a rectangle....(-1 is used to fill the shape)
''' 
	x1, y1------|
	|			|
	|------x2, y2	
'''	   	
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), -1)

#draw a circle....(64 is the radius value)
img = cv2.circle(img, (447, 63), 64, (255, 0, 0), -1)

#let's add some text
#store the font in a variable, and font size is given as 5, cv2.LINE_AA is the line type
font = cv2.FONT_HERSHEY_SIMPLEX 
img = cv2.putText(img, 'OpenCv', (10, 500), font, 5, (255, 255, 255), 10, cv2.LINE_AA)

cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
