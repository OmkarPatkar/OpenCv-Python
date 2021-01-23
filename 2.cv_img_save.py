#The image should be closed if we press esc and on pressing the s key the image should be saved and closed
import cv2
img2 = cv2.imread('lena.jpg', 0)

cv2.imshow('image', img2)

k = cv2.waitKey(0) & 0xFF # & 0xFF is not needed, but if the code is not working on 64bit machinethen use it

if k == 27: #27 == esc key
    cv2.destroyAllWindows()
elif k == ord('s'): # ord is an inbuilt function
    cv2.imwrite('areoo.png', img2)
    cv2.destroyAllWindows()    

