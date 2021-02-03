import cv2
import numpy as np

img = cv2.imread('../Resources/Photos/park.jpg')
cv2.imshow('park', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

#laplacian
lap = cv2.Laplacian(gray, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow('laplacian', lap)

#sobel
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
combined = cv2.bitwise_or(sobelx, sobely)

canny = cv2.Canny(gray, 150, 255)

cv2.imshow('sobel x', sobelx)
cv2.imshow('sobel y', sobely)
cv2.imshow('combined', combined)
cv2.imshow('canny', canny)

cv2.waitKey(0)