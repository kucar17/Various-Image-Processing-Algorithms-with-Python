import cv2
import numpy as np
from matplotlib import pyplot as plt
from idealHighPass import idealHighPass
from highButterworth import highButterworth
from highGaussian import highGaussian
from highLaplacian import highLaplacian

# Reading the image -> Converting to monochrome -> Transffering to Fourier Domain:

img = cv2.imread("airfield-05small-auto.tif")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

m, n = img.shape

ft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
ft_shifted = np.fft.fftshift(ft)

# - IDEAL HIGH-PASS FILTER EXECUTION START -

filter = idealHighPass(m, n, 10)
mag, ang = cv2.cartToPolar(filter[:, :, 0], filter[:, :, 1])

applied = ft_shifted * filter

f_ishift = np.fft.ifftshift(applied)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

fig = plt.figure(figsize=(12, 12))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(mag, cmap="gray")
ax1.title.set_text('Filter Image')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(img_back, cmap="gray")
ax2.title.set_text('Resulting image with Filter')
plt.show()

cv2.imwrite("idealfil.png", mag)

# - IDEAL HIGH-PASS FILTER EXECUTION END -


# - BUTTERWORTH HIGH-PASS FILTER EXECUTION START -

filter = highButterworth(m, n, 190, 2)
mag, ang = cv2.cartToPolar(filter[:, :, 0], filter[:, :, 1])

applied = ft_shifted * filter

f_ishift = np.fft.ifftshift(applied)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

fig = plt.figure(figsize=(12, 12))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(mag, cmap="gray")
ax1.title.set_text('Filter Image')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(img_back, cmap="gray")
ax2.title.set_text('Resulting image with Filter')
plt.show()

cv2.imwrite("butterfil.png", mag)

# - BUTTERWORTH HIGH-PASS FILTER EXECUTION END -


# - GAUSSIAN HIGH-PASS FILTER EXECUTION START -

filter = highGaussian(m, n, 190)
mag, ang = cv2.cartToPolar(filter[:, :, 0], filter[:, :, 1])

applied = ft_shifted * filter

f_ishift = np.fft.ifftshift(applied)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

fig = plt.figure(figsize=(12, 12))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(mag, cmap="gray")
ax1.title.set_text('Filter Image')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(img_back, cmap="gray")
ax2.title.set_text('Resulting image with Filter')
plt.show()

cv2.imwrite("gaussfil.png", mag.astype((np.uint8)))

# - GUASSIAN HIGH-PASS FILTER EXECUTION END -


# - LAPLACIAN HIGH-PASS FILTER EXECUTION START -

filter = highLaplacian(m, n)
mag, ang = cv2.cartToPolar(filter[:, :, 0], filter[:, :, 1])

cv2.imwrite("lap1.png", mag)

applied = ft_shifted * filter

f_ishift = np.fft.ifftshift(applied)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

fig = plt.figure(figsize=(12, 12))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(mag, cmap="gray")
ax1.title.set_text('Filter Image')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(img_back, cmap="gray")
ax2.title.set_text('Resulting image with Filter')
plt.show()

cv2.imwrite("lapfil.png", mag)

# - LAPLACIAN HIGH-PASS FILTER EXECUTION END -