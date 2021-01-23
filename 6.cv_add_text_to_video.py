import cv2
import datetime
from time import strftime, localtime

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'width:' + str(cap.get(3)) + ' height:' + str(cap.get(4))
        datet = str(datetime.datetime.now())
        date_local = strftime("%A, %d %b %Y, %H:%M:%S", localtime())

        frame = cv2.putText(frame, date_local, (10, 50), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow('Video', frame)
        
        if cv2.waitKey(1) == ord('q'):
            break
            
cap.release()
cv2.destroyAllWindows()            
