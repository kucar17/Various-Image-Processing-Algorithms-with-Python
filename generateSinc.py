import numpy as np
import math


def generateSinc():
    t = np.arange(256)

    wave = np.sin(math.pi*t)/math.pi*t
    wave += max(wave)

    img = np.zeros((256, 256))

    for i in range(256):
        for j in range(256):
            img[i][j] = wave[j] * 127

    img = 255 * img

    return img


