import numpy as np

def generateCircle(radius):

    circle = np.zeros((256, 256), dtype=np.float32)

    for i in range(256):
        for j in range(256):
            D = ((i - int(256/2))**2 + (j - int(256/2))**2)**(1/2)

            if D < radius:
                circle[i][j] = 0

            else:
                circle[i][j] = 255

    return circle