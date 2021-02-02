from matplotlib import pyplot as plt
import cv2
import numpy as np

img = cv2.imread("gradient.png", 0)
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


titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, th1 ,th2 ,th3 ,th4, th5]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()