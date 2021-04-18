"""
OpenCV’s deep learning face detector is based on the Single Shot Detector (SSD) 
framework with a ResNet base network (unlike other OpenCV SSDs which typically
use MobileNet as the base network).

It requires two files:
1. Caffe prototxt files
2. Caffe model weight files

"""

# Import the libraries
import numpy as np
import cv2 as cv
import argparse


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required = True, help = 'path to the image')
ap.add_argument('-p', '--prototxt', required =  True, help = 'path to Caffe "deploy" prototxt file')
ap.add_argument('-m', '--model', required = True,	help = 'path to Caffe pre-trained model')
ap.add_argument('-c', '--confidence', type = float, default = 0.5, help = 'minimum probability to filter weak detections')

args = vars(ap.parse_args())

# load our serialized model from disk
print('[INFO] loading model...')
net = cv.dnn.readNetFromCaffe(args['prototxt'], args['model'])

"""
load the input image and construct an input blob for the image by resizing to a fixed 300x300 pixels and then normalizing it.
The dnn.blobFromImage takes care of pre-processing which includes setting the blob dimensions and normalization.
"""
image = cv.imread(args['image'])
(h, w) = image.shape[:2]
blob = cv.dnn.blobFromImage(cv.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0,123.0))

# pass the blob through the network and obtain the detections and predictions
print('[INFO] computing object detection...')
net.setInput(blob) #To detect faces, we pass the blob through the net
detections = net.forward()

#loop over the detections and draw boxes around the detected faces
for i in range(0, detections.shape[2]):
    # extract the confidence (i.e., probability) associated with the prediction
    confidence = detections[0, 0, i, 2]

    # filter out weak detections by ensuring the `confidence` is greater than the minimum confidence.
    if confidence > args['confidence']:
        # compute the (x, y)-coordinates of the bounding box for the object
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY,endX, endY) = box.astype('int')

        # draw the bounding box of the face along with the associated probability
        # confidence text string 
        text = '{:.2f}%'.format(confidence * 100)
        # In case the our text would go off-image (such as when the face detection occurs 
        # at the very top of an image), we shift it down by 10 pixels.
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv.rectangle(image, (startX, startY), (endX, endY), (0 , 0, 255), 2)
        cv.putText(image, text, (startX, y), cv.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)       

# show the output image
cv.imshow('output', image)
cv.waitKey(0)
