import cv2
import numpy as np

# This function receives an image and also a starting, beginning point and resultLevel pixel to perform Gray Level Slicing.
# After the opeation, function records the gray level sliced image to the working directory.
def grayLevelSlice(inimg, beginningPoint, finishPoint, resultLevel):
    # Scanning the each pixel of the original image and assigning result level to corresponding pixel resultLevel,
    # if it is between the range [beginningPoint, finishPoint], and 0, otherwise.
    for i in range(0, inimg.shape[0]):
        for j in range(0, inimg.shape[1]):
            if (inimg[i][j] <= finishPoint and inimg[i][j] >= beginningPoint):
                inimg[i][j] = resultLevel
            else:
                inimg[i][j] = 0
    # Casting the array to 8-bit unsigned integer type to avoid any data-type conflict.
    inimg = inimg.astype((np.uint8))
    # Saving the gray-level sliced image to the working directory and returning:
    cv2.imwrite("gray_level_sliced.jpg", inimg)
    return inimg