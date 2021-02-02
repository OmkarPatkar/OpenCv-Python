#histograms allow us to calculate distribution of pixel in an image
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../Resources/Photos/cats.jpg')
cv2.imshow('cats', img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)

circle = cv2.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 155, -1)

mask = cv2.bitwise_and(gray, gray,mask = circle)
cv2.imshow('mask', mask)

#grayscale histogram
grayhist = cv2.calcHist([gray], [0], mask, [256], [0,256])

plt.figure()
plt.title('grayscale histogram')
plt.xlabel('bins')
plt.ylabel('# of lables')
plt.plot(grayhist)
plt.xlim(0, 256)
plt.show()


cv2.waitKey(0)