import cv2
import numpy as np

# This function receives an image and also a gamme value in order to create the power law transformed image.
# After the transform, function records the quantized image to the working directory.
def powerLawTranform(inimg, power):
    # Applying the power law transformation via. broadcasting
    pTransformedImage = 1 * inimg**power
    # Saving the transformed image to the working directory:
    cv2.imwrite("power_law.jpg", pTransformedImage)