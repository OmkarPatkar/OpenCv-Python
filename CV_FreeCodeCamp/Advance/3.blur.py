import cv2
from numpy.lib.function_base import average, median

img = cv2.imread('../Resources/Photos/cats.jpg')
cv2.imshow('cat', img)

#averaging
average = cv2.blur(img, (3,3))
cv2.imshow('average blur', average)

#gaussian blur
#standard deviation in x direction (0)
gauss = cv2.GaussianBlur(img, (3,3), 0)
cv2.imshow('gaussian blur', gauss)

#median blur
median = cv2.medianBlur(img, 3)
cv2.imshow('median blur', median)

#bilateral blur
#10, 15, 15 = diameter, colors from surrounding, consider pixel from that value 
bilteral = cv2.bilateralFilter(img, 10, 15, 15)
cv2.imshow('bilateral', bilteral)

cv2.waitKey(0)