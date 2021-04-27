import cv2
import numpy as np

from imageSample import sampleImage
from imageQuantize import quantizeImage
from imagePowerLaw import powerLawTranform
from imageGrayLevelSlice import grayLevelSlice
from imageBitPlaneSlice import bitPlaneSlice

# -- IMAGE SAMPLING EXECUTION START --

# Reading the Image
initial_img = cv2.imread("hamburger.jpg")
# Converting the image to greyscale:
initial_img = cv2.cvtColor(initial_img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("hamburger_grey.jpg", initial_img)
# Applying the sampling operation with a sampling rate of 2:
sampleImage(initial_img, 2)

# -- IMAGE SAMPLING EXECUTION FINISH --


# -- IMAGE QUANTIZING EXECUTION START --

# Reading the Image
initial_img = cv2.imread("pcb.jpg")
# Converting the image to greyscale:
initial_img = cv2.cvtColor(initial_img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("pcb_grey.jpg", initial_img)
# Applying the quantizing operation with 32 levels of quantization:
quantizeImage(initial_img, 32)

# -- IMAGE QUANTIZING EXECUTION FINISH --


# -- IMAGE POWER LAF TRANSFORMATION EXECUTION START --

# Reading the Image
initial_img = cv2.imread("mobile_robot.jpg")
# Converting the image to greyscale:
initial_img = cv2.cvtColor(initial_img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("mobile_robot_grey.jpg", initial_img)
# Applying power law transform with gamma equals 1.2 (c constant is set to 1):
powerLawTranform(initial_img, 1.2)

# -- IMAGE POWER LAF TRANSFORMATION EXECUTION FINISH --


# -- IMAGE GRAY-LEVEL SLICING EXECUTION START --

# Reading the Image
initial_img = cv2.imread("cctv_footage.jpg")
# Converting the image to greyscale:
initial_img = cv2.cvtColor(initial_img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("cctv_footage_grey.jpg", initial_img)
# Applying gray level slicing (Assign 255 to pixels between [180, 255], otherwise 0):
grayLevelSlice(initial_img, 180, 255, 255)

# -- IMAGE GRAY-LEVEL SLICING EXECUTION FINISH --


# -- IMAGE BIT-PLANE SLICING EXECUTION START --

# Reading the Image
initial_img = cv2.imread("dragon2.jpg")
# Converting the image to greyscale:
initial_img = cv2.cvtColor(initial_img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("drago2_grey.jpg", initial_img)
# Applying bit-plane slicing for 8-bits:
bitPlaneSlice(initial_img, 8)

# -- IMAGE BIT-PLANE SLICING EXECUTION FINISH --