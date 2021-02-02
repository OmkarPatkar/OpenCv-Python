#thresholdin is a technique to separate image from its background
#thresholding compare each pixel value in the image
import cv2
import numpy as np

#adaptive thresholding works with parts of an image
 
img = cv2.imread("sudoku.png", 0)
#lower thresholding considered as 127 
#and upper thresholding as 255
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

#ADAPTIVE_THRESH_MEAN_C : mean of the neighbourhood area, 11 is block size, 2 is constant c
#ADAPTIVE_THRESH_GAUSSIAN_C : weighted sum of neighbourhood area
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY, 11, 2)

cv2.imshow('image', img)
cv2.imshow("thresholding", th1)
cv2.imshow("ADAPTIVE_THRESH_MEAN_C", th2)
cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", th3)

cv2.waitKey(0)
cv2.destroyAllWindows()