import cv2
import numpy as np
from imagePadding import padImage
from imageCrop import cropImage

# filter -> "x_direct" for x-directional High-Pass Filter,
# "y_direct" for y-directional High-Pass Filter,
# "laplacian" for Laplacian Filter,
# "gaussian" for Gaussian Averaging Filter,
# "uniform" for Uniform Averaging Filter.

def filterImage(inimg, filter):
    # Increasing the dimensions of the image by 2 pixels each side,
    # which corresponds to adding a row/column of zeros on each side of the image:
    paddedImage = padImage(inimg, inimg.shape[0] + 2, inimg.shape[1] + 2)

    # Splitting the image to its color channels to apply 2D filters:
    R, G, B = cv2.split(paddedImage)

    # Choosing the appropriate kernel according to filter input:
    if filter == "x_direct":
        kernel = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)
    elif filter == "y_direct":
        kernel = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=np.float32)
    elif filter == "laplacian":
        kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=np.float32)
    elif filter == "gaussian":
        kernel = np.array([[0.0233, 0.106, 0.0233], [0.106, 0.421, 0.106], [0.0233, 0.106, 0.0233]], dtype=np.float32)
    elif filter == "uniform":
        kernel = np.array([[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]], dtype=np.float32)
    else:
        # If the filter input is not recognized, kernel is going to be (3, 3) zero matrix:
        print("You did not input a valid filter name.")
        kernel =  np.zeros((3, 3), dtype=np.float32)

    # Applying the 2D filter to each color channel of the image:
    filteredImageR = cv2.filter2D(R, -1, kernel)
    filteredImageG = cv2.filter2D(G, -1, kernel)
    filteredImageB = cv2.filter2D(B, -1, kernel)
    
    # Merging the color channels to create the filtered image:
    filteredImage = cv2.merge((filteredImageR, filteredImageG, filteredImageB))

    # Converting the filtered image to unsigned 8-bit integer type:
    filteredImage = filteredImage.astype((np.uint8))

    # Cropping the filtered image by 1 pixels, since it was padded by 1 pixel before:
    cropArray = [1, 1, filteredImage.shape[1] - 1, filteredImage.shape[0] - 1]
    croppedImage = cropImage(filteredImage, cropArray)

    # Converting the filtered, and cropped image to unsigned 8-bit integer type:
    croppedImage = croppedImage.astype((np.uint8))

    return croppedImage