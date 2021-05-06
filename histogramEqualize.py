import cv2
import numpy as np
import math
# importing getHistogram function from the imageHistogram library in order not to
# write the histogram function from scratch:
from imageHistogram import getHistogram


def  histogramEqualization(inimg, bin):
    # Using the pre-defined getHistogram function to get the histogram of the image:
    histogramValues = getHistogram(inimg, bin)
    # Initializing the histogram equalized image:
    equalizedImage = np.zeros((inimg.shape[0], inimg.shape[0]))

    ratio = 256 / bin

    pn = histogramValues / (inimg.shape[0] * inimg.shape[1])

    for i in range(equalizedImage.shape[0]):
        for j in range(equalizedImage.shape[1]):
            equalizedImage[i][j] = (bin - 1) * sumUntilLimit(pn, int(inimg[i][j]/ratio))

    equalizedImage = equalizedImage.astype((np.uint8))
    return equalizedImage

def sumUntilLimit(array, limit):
    sum = 0
    for i in range(limit):
        sum += array[i]

    return sum