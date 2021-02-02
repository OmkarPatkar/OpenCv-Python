import cv2
import numpy as np

blank = np.zeros((400, 400), dtype = 'uint8')

rectangle = cv2.rectangle(blank.copy(), (30,30), (370, 370), 255, -1)
circle = cv2.circle(blank.copy(), (200, 200), 200, 255, -1)

cv2.imshow("rectangle", rectangle)
cv2.imshow("circle", circle)

#intersecting regions
bitand = cv2.bitwise_and(rectangle, circle)
cv2.imshow("bitwise and", bitand)

#non intersecting regions and intersecting regions
bitor = cv2.bitwise_or(rectangle, circle)
cv2.imshow("bitwise or", bitor)

#non intersecting regions
bitxor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("bitwise xor", bitxor)

bitnot = cv2.bitwise_not(rectangle)
cv2.imshow("bitwise not", bitnot)

cv2.waitKey(0)