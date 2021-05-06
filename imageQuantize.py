import cv2
import numpy as np

# This function receives an image and also a quantization level in order to create the quantized image.
# After the quantizing process, function records the quantized image to the working directory.
def quantizeImage(inimg, quantizationLevel):
    # Initializing the quantized image:
    quantizedImage = np.zeros((inimg.shape[0], inimg.shape[1]),dtype=np.uint16)
    # Defining the quantization levels:
    # 
    quantizationRange = createRange(0, 255, int(256/quantizationLevel))
    # Scanning the each pixel of the original image,
    # and assigning the quantized pixel value to the corresponding pixel:
    for i in range(0, inimg.shape[0]):
        for j in range(0, inimg.shape[1]):
            index = findClosestMatch(inimg[i][j], quantizationRange)
            quantizedImage[i][j] = quantizationRange[index]
    # Casting the array to 8-bit unsigned integer type to avoid any data-type conflict. 
    quantizedImage = quantizedImage.astype((np.uint8))
    # Saving the quantized image to the working directory and returning:
    cv2.imwrite("quantized.jpg", quantizedImage)
    return quantizedImage


# This is a helper function for the quantizeImage function, which finds the corresponding pixel value,
# given a set of quantization levels. Function uses broadcasting in order to yield efficiency.
def findClosestMatch(pixelValue, quantizationLevel):
    errorArray = []
    errorArray.append(abs(pixelValue - quantizationLevel))
    quantizationIndex = np.argmin(errorArray)

    return quantizationIndex

# This is a helper function for the quantizeImage function, which creates the quantization levels,
# given a number of quantization levels.
def createRange(start, stop, step):
    length = int((stop - start)/2 + 1)
    quantizationLevels = []

    for i in range(length):
        quantizationLevels.append(i*step)

    return quantizationLevels
