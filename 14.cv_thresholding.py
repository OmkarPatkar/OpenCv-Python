#thresholdin is a technique to separate image from its background
#thresholding compare each pixel value in the image
import cv2
import numpy as np

img = cv2.imread("../other/gradient.png", 0)
#lower thresholding considered as 127 
#and upper thresholding as 255
# if the pixel value in the image is lower than 127 then the pixel is assigned to 255  
# if the pixel value in the image is upper than 127 then the pixel is assigned to 0  
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
#upto the threshold will not change
ret, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
#if the pixel value is less than 127 then its 0
ret, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('image', img)
cv2.imshow("th1", th1)
cv2.imshow("th1", th2)
cv2.imshow("th1", th3)
cv2.imshow("th1", th4)
cv2.imshow("th5", th5)

cv2.waitKey(0)
cv2.destroyAllWindows()