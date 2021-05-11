import numpy as np
import cv2

# The function receives an initial img, a kernel for low-pass filter, and a gain value for the mask,
# and returns the output image which went through the unsharp mask transformation.

def unsharpMasking(inimg, lowPassFilter, k):

    # Splitting the image into three, 2D color channels:
    channel1, channel2, channel3 = cv2.split(inimg)
    # Applying the low-pass filter kernel to each color channel:
    channel1 = cv2.filter2D(channel1, -1, lowPassFilter)
    channel2 = cv2.filter2D(channel2, -1, lowPassFilter)
    channel3 = cv2.filter2D(channel3, -1, lowPassFilter)
    # Merging the three channels to create the low-pass filter applied image:
    lowPassed = cv2.merge((channel1, channel2, channel2))
    # Subtracting the low-pass filter applied image from the original image, to get the mask:
    mask = inimg - lowPassed
    # Multiplying the mask by a gain, and then adding to the original image to get the output image:
    unsharpenedImage = inimg + k * mask
    # Converting the intensity values of the output image to 8-bit unsigned integers:
    unsharpenedImage = unsharpenedImage.astype((np.uint8))

    return unsharpenedImage