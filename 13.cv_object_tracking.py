import cv2
import numpy as np

def nothing(x):
    print(x)

cap = cv2.VideoCapture(0);

cv2.namedWindow('image')

#create trackbar to adjust hue of lower and upper bound
#lh: lower hue, ls: lower saturation, lv: lower value
#uh: upper hue, us: upper saturation, uv: upper value
cv2.createTrackbar('lh', 'image', 0, 255, nothing)
cv2.createTrackbar('ls', 'image', 0, 255, nothing)
cv2.createTrackbar('lv', 'image', 0, 255, nothing)
cv2.createTrackbar('uh', 'image', 255, 255, nothing)
cv2.createTrackbar('us', 'image', 255, 255, nothing)
cv2.createTrackbar('uv', 'image', 255, 255, nothing)

while(1):
    #frame = cv2.imread('smarties.png')
    _, frame = cap.read()
    
    #convert img to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lh = cv2.getTrackbarPos('lh', 'image')
    ls = cv2.getTrackbarPos('ls', 'image')
    lv = cv2.getTrackbarPos('lv', 'image')

    uh = cv2.getTrackbarPos('uh', 'image')
    us = cv2.getTrackbarPos('us', 'image')
    uv = cv2.getTrackbarPos('uv', 'image')

    #lower and upper bound for blue color
    #l_b = np.array([110, 50, 50])
    #u_b = np.array([130, 255,255])

    l_b = np.array([lh, ls, lv])
    u_b = np.array([uh, us, uv])
    
    #to get the  blue color
    mask = cv2.inRange(hsv, l_b, u_b)
    
    #to get the bitwise and  of the img
    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()