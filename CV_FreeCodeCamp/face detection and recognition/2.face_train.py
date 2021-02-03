import os
import cv2 as cv
import numpy as np

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIR = r'/home/patkar/git/venv/python/OpenCv-Python/CV_FreeCodeCamp/Resources/Faces/train/'

haarcascade = cv.CascadeClassifier('haar_face.xml') #download classifier fron opencv repo

features = [] #img array of faces
labels = [] #labels of faces

def create_train():
    for person in people:  #loop through every person in the people list
        path = os.path.join(DIR, person) #goes to each folder and grab the path of that folder
        label = people.index(person) #giving index to people list

        for img in os.listdir(path): # looping over evry image in particular folder
            img_path = os.path.join(path, img)  # grabing the path of the image

            img_array = cv.imread(img_path) #reading the images
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY) # convering image to grayscale

            faces_rect = haarcascade.detectMultiScale(gray, 1.1, 4) #detecting faces

            for (x, y, w, h) in faces_rect: #loop over every face in faces_rect
                faces_roi = gray[y: y+h, x: x+w] #cropping the face from image
                features.append(faces_roi) #appending faces to feature list
                labels.append(label) # appending labels to label list

create_train()

print('training complete')

print(f'length of the features = {len(features)}')
print(f'length of the labels = {len(labels)}')

#converting features and labels to array
features = np.array(features, dtype = 'object')
labels = np.array(labels)

#instantiate face rrecognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create() 

#train the recognizer on the feature and labels list
face_recognizer.train(features, labels)

#save features and labels list
np.save('features.npy', features)
np.save('labels.npy', labels)

#save the model
face_recognizer.save('face_trained.yml')