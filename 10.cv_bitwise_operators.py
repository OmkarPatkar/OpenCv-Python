import cv2
import numpy as np

img1 = np.zeros((512, 512, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = cv2.imread("block.jpg")
img2= cv2.resize(img2, (512, 512))

bitAnd = cv2.bitwise_and(img2, img1)
'''
bitOr = cv2.bitwise_or(img2, img1)
bitXor = cv2.bitwise_xor(img1, img2)
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)
'''

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("bitand", bitAnd)
'''
cv2.imshow("bitor", bitOr)
cv2.imshow("bitxor", bitXor)
cv2.imshow("bitnot1", bitNot1)
cv2.imshow("bitnot2", bitNot2)
'''
cv2.waitKey()
cv2.destroyAllWindows()