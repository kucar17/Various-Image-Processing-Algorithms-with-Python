import cv2
import numpy as np
from imageHistogram import getHistogram
from histogramEqualize import histogramEqualization


# -- IMAGE HISTOGRAM EXECUTION START --

# Reading the Image
initial_img = cv2.imread("Fig3.15(a)3.jpg")
# Converting the image to greyscale:
initial_img = cv2.cvtColor(initial_img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("Fig3.15(a)3_grey.jpg", initial_img)
cv2.imshow("Original Image", initial_img)
# Applying getHistogram function to get the histogram with 256 histogram levels:
histogramValues = getHistogram(initial_img, 256)
cv2.waitKey(0)
cv2.destroyAllWindows()


# -- IMAGE HISTOGRAM EXECUTION END --

# -- MAGE HISTOGRAM EQUALIZATION START --

# We are going to use the image which we used for image histogram above:
cv2.imshow("Original Image", initial_img)
# Applying histogram equalization and obtaining the transformed image:
outimg = histogramEqualization(initial_img, 256)
cv2.imshow("Histogram equalized image with 256 bin values", outimg)
cv2.imwrite("Fig3.15(a)3_eq.jpg", outimg)
cv2.waitKey(0)
cv2.destroyAllWindows()