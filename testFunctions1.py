import cv2
import numpy as np

from imageSample import sampleImage
from imageQuantize import quantizeImage
from imagePowerLaw import powerLawTranform
from imageGrayLevelSlice import grayLevelSlice
from imageBitPlaneSlice import bitPlaneSlice

# -- IMAGE SAMPLING EXECUTION START --

# Reading the Image
initial_img = cv2.imread("PEPPERS.TIF")
# Converting the image to greyscale:
initial_img = cv2.cvtColor(initial_img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("PEPPERS_GRAY.TIF", initial_img)
cv2.imshow("Original Image", initial_img)
# Applying the sampling operation with a sampling rate of 2:
sampledImage = sampleImage(initial_img, 2)
cv2.imwrite("sampled.png", sampledImage)
cv2.imshow("Sampled Image with a sampling rate of 2", sampledImage)
cv2.waitKey(0)
cv2.destroyAllWindows()


# -- IMAGE SAMPLING EXECUTION FINISH --


# -- IMAGE QUANTIZING EXECUTION START --

# Reading the Image
initial_img = cv2.imread("MANDRILL.TIF")
# Converting the image to greyscale:
initial_img = cv2.cvtColor(initial_img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("MANDRILL_GREY.TIF", initial_img)
cv2.imshow("Original Image", initial_img)
# Applying the quantizing operation with 32 levels of quantization:
quantizedImage = quantizeImage(initial_img, 32)
cv2.imwrite("quantized.png", quantizedImage)
cv2.imshow("Quantized Image with 32 quantization levels", quantizedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()


# -- IMAGE QUANTIZING EXECUTION FINISH --


# -- IMAGE POWER LAF TRANSFORMATION EXECUTION START --

# Reading the Image
initial_img = cv2.imread("ireland-02small.tif")
# Converting the image to greyscale:
initial_img = cv2.cvtColor(initial_img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("ireland-02small_gray.tif", initial_img)
cv2.imshow("Original Image", initial_img)
# Applying power law transform with gamma equals 4:
powerLawTransformed = powerLawTranform(initial_img, 4)
cv2.imwrite("power_law_transformed.png", powerLawTransformed)
cv2.imshow("Power Law Transformed image with gamma = 4", powerLawTransformed)
cv2.waitKey(0)
cv2.destroyAllWindows()


# -- IMAGE POWER LAF TRANSFORMATION EXECUTION FINISH --


# -- IMAGE GRAY-LEVEL SLICING EXECUTION START --

# Reading the Image
initial_img = cv2.imread("BLOCKS.TIF")
# Converting the image to greyscale:
initial_img = cv2.cvtColor(initial_img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("BLOCKS_GRAY.TIF", initial_img)
cv2.imshow("Original Image", initial_img)
# Applying gray level slicing (Assign 255 to pixels between [80, 255], otherwise 0):
grayLevelSliced = grayLevelSlice(initial_img, 80, 255, 255)
cv2.imwrite("gray_level_sliced1.png", grayLevelSliced)
cv2.imshow("Gray Level Sliced Image ([80 - 255 -> 255, else -> 0])", grayLevelSliced)
cv2.waitKey(0)
cv2.destroyAllWindows()


# -- IMAGE GRAY-LEVEL SLICING EXECUTION FINISH --


# -- IMAGE BIT-PLANE SLICING EXECUTION START --

# Reading the Image
initial_img = cv2.imread("F14.TIF")
# Converting the image to greyscale:
initial_img = cv2.cvtColor(initial_img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("F14_GRAY.TIF", initial_img)
cv2.imshow("Original Image", initial_img)
# Applying bit-plane slicing and receiving the 7th bit:
bitPlaneSliced = bitPlaneSlice(initial_img, 7)
cv2.imwrite("bit_level_sliced.png", bitPlaneSliced)
cv2.imshow("Plane 7 of the Bit Plane Sliced Image", bitPlaneSliced)
cv2.waitKey(0)
cv2.destroyAllWindows()

# -- IMAGE BIT-PLANE SLICING EXECUTION FINISH --

