import numpy as np

def padImage(inimg, nrp, ncp):
    # Initializing the padded image with zeros (black):
    paddedImage = np.zeros((nrp, ncp, 3))

    # Calculating the starting grid (pixel) where the first pixel of the original image will be placed:
    padStart1 = int((ncp / 2) - (inimg.shape[1] / 2))
    padStart2 = int((nrp / 2) - (inimg.shape[0] / 2))

    # Assigning the pixels of the original image to the corresponding part of the padded image:
    paddedImage[padStart2: padStart2 + inimg.shape[0],padStart1: padStart1 + int(inimg.shape[1])] = inimg

    # Converting the pixels in the padded image to 8-bit integer type, just in case:
    paddedImage = paddedImage.astype((np.uint8))

    return paddedImage

