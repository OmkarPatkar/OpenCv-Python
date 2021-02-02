#histograms allow us to calculate distribution of pixel in an image
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../Resources/Photos/cats.jpg')
cv2.imshow('cats', img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')

mask = cv2.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 155, -1)

# color histogram
masked = cv2.bitwise_and(img, img, mask = mask)
cv2.imshow("mask1", masked)

plt.figure()
plt.title('color histogram ')
plt.xlabel('bins')
plt.ylabel('# of pixels')

colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv2.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist, color = col)
    plt.xlim([0, 256])
plt.show()


cv2.waitKey(0)