import numpy as np
from generateSine import generateSine
from generateCircle import generateCircle
from generateRectangle import generateRectangle
from generateSinc import generateSinc
from matplotlib import pyplot as plt
import cv2
import numpy as np


img = generateSine(6, 0, orientation="horizontal")

ft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
ft_shifted = np.fft.fftshift(ft)
mag = 20 * np.log(cv2.magnitude(ft_shifted[:, :, 0], ft_shifted[:, :, 1]))

fig = plt.figure(figsize=(12, 12))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img, cmap="gray")
ax1.title.set_text('Input Image')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(mag, cmap="gray")
ax2.title.set_text('FFT of image')
plt.show()

img = generateCircle(120)

ft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
ft_shifted = np.fft.fftshift(ft)
mag = 20 * np.log(cv2.magnitude(ft_shifted[:, :, 0], ft_shifted[:, :, 1]))

fig = plt.figure(figsize=(12, 12))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img, cmap="gray")
ax1.title.set_text('Input Image')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(mag, cmap="gray")
ax2.title.set_text('FFT of image')
plt.show()

img = generateRectangle(90, 90)

ft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
ft_shifted = np.fft.fftshift(ft)
mag = 20 * np.log(cv2.magnitude(ft_shifted[:, :, 0], ft_shifted[:, :, 1]))

fig = plt.figure(figsize=(12, 12))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img, cmap="gray")
ax1.title.set_text('Input Image')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(mag, cmap="gray")
ax2.title.set_text('FFT of image')
plt.show()
img = generateSinc()

ft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
ft_shifted = np.fft.fftshift(ft)
mag = 20 * np.log(cv2.magnitude(ft_shifted[:, :, 0], ft_shifted[:, :, 1]))

fig = plt.figure(figsize=(12, 12))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img, cmap="gray")
ax1.title.set_text('Input Image')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(mag, cmap="gray")
ax2.title.set_text('FFT of image')
plt.show()