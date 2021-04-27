import cv2
import numpy as np

def sampleImage(mono_image, samplingRatio):
    # This function receives an image and also a sampling ratio in order to create the sampled image.
    # After the sampling process, function records the sampled image to the working directory.

    # Initializing the sampled image:
    sampledImage = 127 * np.ones((mono_image.shape[0], mono_image.shape[1]),dtype=np.uint16)
    # Scanning the original image, according to the sample rate,
    # and assigning the pixel value to the corresponding pixel:
    for i in range(0, mono_image.shape[0], samplingRatio):
        for j in range(0, mono_image.shape[1], samplingRatio):
            sampledImage[i][j] = mono_image[i][j]
    # Saving the sampled image to the working directory:
    cv2.imwrite("sampled.jpg", sampledImage)