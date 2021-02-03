import cv2

img = cv2.imread('../Resources/Photos/group 1.jpg')
cv2.imshow('group', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

haarcascade = cv2.CascadeClassifier('haar_face.xml')

faces_rect = haarcascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 1)

print(f'number of faces found = {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness = 2)
    cv2.imshow('detected face', img)

cv2.waitKey(0)