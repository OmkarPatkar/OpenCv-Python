import cv2
import matplotlib.pyplot as plt

img = cv2.imread('../Resources/Photos/park.jpg')
cv2.imshow('park', img)

#plt.imshow(img)
#plt.show()

#BGR to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

#BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('hsv', hsv)

#BGR to L*a*b
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow('lab', lab)

#BGR to RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('rgb', rgb)

#HSV to BGR
hsv_bgr = cv2.cvtColor(img, cv2.COLOR_HLS2BGR)
cv2.imshow('hsv --> bgr', hsv_bgr)

#lab to bgr
lab_bgr = cv2.cvtColor(img, cv2.COLOR_LAB2RGB)
cv2.imshow('lab --> bgr', lab_bgr)

# we can not convert grayscale to hsv directly,
#  we have to first convert grayscale to bgr and then to hsv

cv2.waitKey(0)