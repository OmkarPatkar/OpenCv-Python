import cv2
import numpy as np 

img = cv2.imread('../Resources/Photos/cats.jpg')
cv2.imshow("cats", img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')
cv2.imshow("blank", blank)

mask = cv2.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv2.imshow("mask", mask)

masked = cv2.bitwise_and(img, img, mask = mask)
cv2.imshow("masked image", masked)

circle = cv2.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 200, 255, -1)
rectangle = cv2.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
weirdshape = cv2.bitwise_and(circle, rectangle)

wmasked = cv2.bitwise_and(img, img, mask = weirdshape)
cv2.imshow("weired masked image", wmasked)

cv2.waitKey(0)