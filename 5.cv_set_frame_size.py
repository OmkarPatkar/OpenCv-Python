import cv2

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#the default value for width is 3, and for height the value is 4
cap.set(3, 1208) #will take the width as 1280
cap.set(4, 720)

print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
    
    	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    	cv2.imshow('Video', gray)
    	
    	if cv2.waitKey(1) == ord('q'):
        	break
        
cap.release()
cv2.destroyAllWindows()
