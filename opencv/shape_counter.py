# import libraries
import argparse
import cv2 as cv
import imutils

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input', required = True, help = 'Path to the input image.')
ap.add_argument('-o', '--output', required = True, help = ' Path to the output image.')
args = vars(ap.parse_args())

''' vars  on the object to turn the parsed command line
 arguments into a Python dictionary where the key to the 
 dictionary is the name of the command line argument and 
 the value is value of the dictionary supplied for the 
 command line argument.
 '''

# Load the input image
image = cv.imread(args['input'])

# convert the image to grayscale, blur it, and threshold it
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(gray, (5,5), 0)
thresh = cv.threshold(blurred, 60, 255, cv.THRESH_BINARY)[1]

# extract contours from the image
cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# loop over the contours and draw them on the input image
for c in cnts:
    cv.drawContours(image, [c], -1, (255, 0, 0), 2)

# display the total number of shapes on the image
text = f"I found {len(cnts)} total shapes."
cv.putText(image, text, (20,20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

# write the output image to disk
cv.imwrite(args['output'], image)
