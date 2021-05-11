import numpy as np

# The function takes two parameters -> initial img and the cropArray.
# cropArray specifies two points (upper left, and bottom right points of the cropped version of the image).
# cropArray has the following structure -> [horizontal1, vertical1, horizontal2, vertical2]
def cropImage(inimg, cropArray):
    
    # Initializing the cropped image; sizes are vertical2 - vertical1 and horizontal2 - horizontal1:
    croppedImage = np.zeros((cropArray[3] - cropArray[1], cropArray[2] - cropArray[0], 3))

    # Substituting the corresponding pixels from the inimg with the corresponding pixels of the croppedImage:
    croppedImage[0 : cropArray[3] - cropArray[1], 0 : cropArray[2] - cropArray[0]] = inimg[cropArray[1] : cropArray[3], cropArray[0] : cropArray[2]]

    # Converting the image pixels to unsigned 8-bit integers to avoid any conflict:
    croppedImage = croppedImage.astype((np.uint8))
    
    return croppedImage


