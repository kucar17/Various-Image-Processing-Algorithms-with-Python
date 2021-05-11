import cv2
import numpy as np

# Function receives 3 inputs, the initial image to be filtered, the filter size (n)
# which will form an (n, n) 2D filter matrix, and the type of statistics
# which is going to be used for the image:

def orderStFiltering(inimg, filterSize, typeOfStatistics):

    if typeOfStatistics == "median":
        #Applying Median Filter to the image with the specified filterSize:
        filteredImage = cv2.medianBlur(inimg, filterSize)
    
    elif typeOfStatistics == "min":
        #Applying Median Filter to the image with the specified filterSize and kernel:
        kernel = np.ones((filterSize, filterSize))
        filteredImage = cv2.erode(inimg, kernel)

    elif typeOfStatistics == "max":
        #Applying Median Filter to the image with the specified filterSize and kernel:
        kernel = np.ones((filterSize, filterSize))
        filteredImage = cv2.dilate(inimg, kernel)

    else:
        # If an unexpected input is given for the statistics type, filter will be set to zero matrix:
        print("You did not input a valid filter name!")
        filteredImage = np.zeros((inimg.shape[0], inimg.shape[1]))

    # Converting the output image to unsigned 8-bit integer type:
    filteredImage = filteredImage.astype((np.uint8))

    return filteredImage

