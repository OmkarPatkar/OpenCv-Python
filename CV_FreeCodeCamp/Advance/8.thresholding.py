import cv2

img = cv2.imread('../Resources/Photos/cats.jpg')
cv2.imshow('cats', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

#simple thresholding
threshold, thresh = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
cv2.imshow('simple threshold', thresh)

threshold, threshinv = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('simple threshold inverse', threshinv)

#adaptive thresholding
adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 3)
cv2.imshow('adaptive', adaptive)

cv2.waitKey(0)