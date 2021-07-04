# Import library toconvert pdfs to images
from pdf2image import convert_from_path
import argparse
import os
import cv2 as cv
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-p', '--path', required = True, help = 'path to pdf file with its name')
args = vars(ap.parse_args())

# Load the files and convert them to images
pdfs = args['path']
pages = convert_from_path(pdfs, 350, poppler_path = r"C:\poppler-21.03.0\Library\bin")

# Mark the region of interest in the pdf file
def Mark_roi(image_path):

    # Load the images
    img = cv.imread(image_path)

    # define threshold of regions to ignore
    THRESHOLD_REGION_IGNORE = 40

    # Convert the images to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Blurring the images
    blur = cv.GaussianBlur(gray, (9, 9), 0)

    #
    threshold = cv.adaptiveThreshold(blur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 30)

    # Dilate to combine adjacent text contours
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (9, 9))
    dilate = cv.dilate(threshold, kernel, iterations = 4)

    # Find contours, highlight text areas, and extract ROIs
    cnts = cv.findContours(dilate, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    line_items_cordinates = []
    for c in cnts:
        area = cv.contourArea(c)
        x, y, w, h = cv.boundingRect(c)

        if w < THRESHOLD_REGION_IGNORE or h < THRESHOLD_REGION_IGNORE:
            continue

        img = cv.rectangle(img, (x, y), (x + w, y + h), color=(255, 0, 255), thickness=3)
        line_items_cordinates.append([(x, y), (x + w, y + h)])

    return img, line_items_cordinates

# create folders to store images
if not os.path.exists('images/pdf2image'):
    os.makedirs('images/pdf2image')

if not os.path.exists('images/bounding_images'):
    os.makedirs('images/bounding_images')

# Run a loop to convert the pdf to images
i = 1
j = 1

for page in pages:
    image_name = "Page_" + str(i) + ".jpg"
    folder = "./images/pdf2image/" + str(image_name)
    page.save(folder, "JPEG")
    print(f"{image_name} created successfully")

    # Put bounding box around the text in the images
    bounding_images = "image_" + str(j) + ".jpg"
    pic = "./images/bounding_images/" + str(bounding_images)
    image, line_items_cordinates = Mark_roi(folder)
    a_i = Image.fromarray(image)
    a_i.save(pic, "JPEG")
    print(f"{bounding_images} bounding box created successfully")
    i += 1
    j += 1

print("Done successfully, Yay!")