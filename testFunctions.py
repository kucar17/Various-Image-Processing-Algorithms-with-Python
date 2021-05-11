import cv2
import numpy as np
from imagePadding import padImage
from imageCrop import cropImage
from imageFilter import filterImage
from imageUnsharpMask import unsharpMasking
from orderStFilter import orderStFiltering

# -- IMAGE PADDING EXECUTION START --

# Reading the image
img = cv2.imread("PEPPERS.TIF")

# Applying padding with a 700 x 800, plane (which does not have the same aspect ratio with the original image):
paddedImage = padImage(img, 700, 800)

cv2.imwrite("padded.png", paddedImage)
cv2.imshow("padded", paddedImage)
cv2.waitKey(0)
cv2.destroyAllWindows

# -- IMAGE PADDING EXECUTION FINISH --


# -- IMAGE CROPPING EXECUTION START --

# Reading the image
img = cv2.imread("MANDRILL.TIF")

# Creating the arbitrary crop array for cropping operation:
cropArray = [10, 50, 190, 254]
croppedImage = cropImage(img, cropArray)

cv2.imwrite("cropped.png", croppedImage)
cv2.imshow("cropped", croppedImage)
cv2.waitKey(0)
cv2.destroyAllWindows

# -- IMAGE CROPPING EXECUTION FINISH --


# -- IMAGE FILTERING EXECUTION START --

# Reading the image
img = cv2.imread("piran-small.tif")

# Appyling Uniform Averaging Filter to the image:
filteredImage = filterImage(img, filter="uniform")

cv2.imwrite("filtered.png", filteredImage)
cv2.imshow("filtered", filteredImage)
cv2.waitKey(0)
cv2.destroyAllWindows

# -- IMAGE FILTERING EXECUTION FINISH --


# -- IMAGE ORDERST FILTERING EXECUTION START --

# Reading the input image:
img = cv2.imread("harley-engine.tif")
# Appyling maximum filter to the image:
orderStFiltered = orderStFiltering(img, 5, "max")
cv2.imwrite("orderStFiltered.png", orderStFiltered)
cv2.imshow("Input Image", img)
cv2.imshow("Output Image", orderStFiltered)
cv2.waitKey()
cv2.destroyAllWindows()

# -- IMAGE ORDERST FILTERING EXECUTION FINISH --


# -- IMAGE UNSHARP MASKING EXECUTION START --

# Reading the input image:
img = cv2.imread("DOTS.TIF")
# Defining the low-pass filter kernel:
lowpass = (1/25) * np.ones((5, 5), dtype=np.float32)
# Applying unsharpMasking to the image:
unSharpened = unsharpMasking(img, lowpass, 2)
# Displaying the results
cv2.imwrite("unsharpened.png", unSharpened)
cv2.imshow("Input Image", img)
cv2.imshow("Output Image", unSharpened)
cv2.waitKey()
cv2.destroyAllWindows()

# -- IMAGE UNSHARP MASKING EXECUTION FINISH --



