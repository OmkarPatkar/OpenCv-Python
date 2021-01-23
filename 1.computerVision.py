#import opencv
#from google.colab.patches import cv2_imshow ||..."when using colab run this code and use cv2_imshow instead of cv2.imshow"...||
import cv2

#read image
img = cv2.imread('lena.jpg', 0)
print(img)

cv2.imshow('image', img)
cv2.waitKey(5000) #use this to display the img for a specific time
cv2.destroyAllWindows()

cv2.imwrite('lenacopy.png', img) #makes a copy of the img
	
