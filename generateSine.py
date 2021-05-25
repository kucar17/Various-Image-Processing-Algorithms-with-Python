import numpy as np
import math


def generateSine(period, shift, orientation):
    t = np.arange(256)

    wave = np.sin(2*np.pi*t/period + shift)
    wave += max(wave)

    #img = np.zeros((256, 256))
    """
    for i in range(256):
        for j in range(256):
            img[i][j] = wave[j] * 127
    """

    img = np.array([[wave[j]*127 for j in range(256)] for i in range(256)], dtype=np.uint8)       

    if orientation == "vertical":
        img = np.rot90(img)

    #img = 255 * img

    return img


