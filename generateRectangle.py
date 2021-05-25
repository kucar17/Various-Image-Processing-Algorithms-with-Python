import numpy as np

def generateRectangle(vertical, horizontal):

    rectangle = np.zeros((256, 256), dtype=np.float32)

    for i in range(256):
        for j in range(256):
            #D = ((i - int(256/2))**2 + (j - int(256/2))**2)**(1/2)
            disShort = abs(j - (256/2))
            disLong = abs(i - (256/2))

            if disLong < vertical/2 and disShort < horizontal/2:
                rectangle[i][j] = 0

            else:
                rectangle[i][j] = 255

    return rectangle