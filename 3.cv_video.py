import cv2

cap = cv2.VideoCapture(0) # 0 is the camera index
#cap = cv2.VideoCapture("file.avi")

#four byte code 
fourcc = cv2.VideoWriter_fourcc(*'XVID')

#to save the video
out = cv2.VideoWriter("outvideo.avi", fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read() #ret: return true if file is available, frame: captures video frames
    
    if ret == True:
    
    	#print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    	#print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    	
    	out.write(frame)
    	
    	#convert the video to grayscale
    	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    	cv2.imshow("Video Frame", gray)
    	
    	if cv2.waitKey(1) & 0xFF == ord('q'):
        	break
    	
cap.release() #release the resources
cv2.destroyAllWindows()
