import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

# Defining a low-pass Gaussian Filter
def lowGauss(M, N, D0):
    filter = np.ones((M, N, 2), dtype=np.float32)
    
    # Scanning through each pixel and calculating the distance of each pixel
    # to the image center. After the distance is calculated, operation on line 17
    # will be applied.
    for i in range(M):
        for j in range(N):
            D = ((i - int(M/2))**2 + (j - int(N/2))**2)**(1/2)

            filter[i][j] = math.exp(-(D**2) / ((2)*D0**2))

    return filter

# Reading the image -> converting to monochrome -> Transffering to Fourier Domain:
img = cv2.imread("print-pattern.tif")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

m, n = img.shape

ft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
ft_shifted = np.fft.fftshift(ft)


# Defining the Low-Pass Gaussian Filter:
filter = lowGauss(m, n, 65)
# Applying the filter:
applied = ft_shifted * filter

# Applying Inverse Fourier Transform:
f_ishift = np.fft.ifftshift(applied)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

# Plotting the original and resulting images:
fig = plt.figure(figsize=(12, 12))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img, cmap="gray")
ax1.title.set_text('Original Image')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(img_back, cmap="gray")
ax2.title.set_text('Resulting image after Low-Pass Gaussian Filter')
plt.show()