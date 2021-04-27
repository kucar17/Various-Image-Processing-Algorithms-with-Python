import cv2
import numpy as np

# This function receives an image and also a bitPlaneNumber to perform Bit-Level Slicing.
# After the operation, function records the bitlevel sliced image to the working directory.
def bitPlaneSlice(inimg, bitPlaneNumber):
    bitPlaneNumber = bitPlaneNumber + 1
    bitPlaneImg = np.zeros((inimg.shape[0], inimg.shape[1]), dtype=str)
    # Finding the binary equivalent values of each pixel in the image, and then
    # assigning the ith bit of the binary-valued pixels to the corresponding pixel in each bitPlane (MSB -> LSB)
    # (zfill is used to make sure that binary representations are going to be in the required number of bits.)
    for i in range(bitPlaneNumber):

        if (i == bitPlaneNumber):
            break

        for j in range(0, inimg.shape[0]):
            for k in range(0, inimg.shape[1]):
                bitPlaneImg[j][k] = bin(inimg[j][k])[2:].zfill(bitPlaneNumber)[i]

                if (bitPlaneImg[j][k] == 1):
                    bitPlaneImg[j][k] = 255
                else:
                    bitPlaneImg[j][k] = 0
        # Casting the array to integer type to avoid any data-type conflict.            
        bitPlaneImg = bitPlaneImg.astype(int)
        # Saving the particular bit-plane image to the working directory:
        cv2.imwrite("bitPlane" + str(bitPlaneNumber - (i+1)) + ".jpg",bitPlaneImg)
