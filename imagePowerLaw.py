import cv2
import numpy as np

# This function receives an image and also a gamme value in order to create the power law transformed image.
# After the transform, function records the quantized image to the working directory.
def powerLawTranform(inimg, power):
    # Applying the power law transformation via. broadcasting
    pTransformedImage = np.array(255*(inimg / 255) ** power)
    # Casting the array to 8-bit unsigned integer type to avoid any data-type conflict.
    pTransformedImage = pTransformedImage.astype((np.uint8))
    # Saving the transformed image to the working directory and returning:
    cv2.imwrite("power_law.jpg", pTransformedImage)
    return pTransformedImage