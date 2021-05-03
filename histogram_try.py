import cv2
import numpy as np
import matplotlib.pyplot as plt

def getHistogram(image, bin):  

    # Initializing the dictionary and the first key of it:
    rangeDict = {
    "set0": []
    }

    # Acquiring the increment value:
    increment = int(256 / bin)

    # Initializing the start and stop values:
    start = 0
    stop = start + increment
    
    while True:

        # Adding the numbers to the key one after another in a single list, according to the user input:
        for i in range(start, stop):
            #print(start)
            #print(stop)
            arrayToAppend = np.arange(start, stop, 1).tolist()

        rangeDict["set" + str(int(start/increment))] = arrayToAppend

        # When 255 is reached in the dictionary, loop will terminate:
        if rangeDict["set" + str(int(start/increment))][-1] == 255:
            break

        else:
            # Assigning the greatest value in the most recently added key to the start:
            start = rangeDict["set" + str(int(start/increment))][-1] + 1
            # Assigning start, plus the increment
            stop = start + increment
            # Initializing the next key:
            #rangeDict["set" + str(i + 1)] = []
    # Printing the dictionary for checking:
    #print(rangeDict)

    for i in range(len(rangeDict)):
        rangeDict["set" + str(i)].append(0)

    plotArray = np.zeros((bin,), dtype=int)

    for i in range(image.shape[0]):
        print("i = " + str(i))
        for j in range(image.shape[1]):
            #print("j = " + str(j))
            for k in range(len(rangeDict)):
                #print("k = " + str(k))
                for t in range(len(rangeDict["set" + str(k)])):
                    #print("t = " + str(t))
                    if image[i][j] == rangeDict["set" + str(k)][t]:
                        #rangeDict["set" + str(i)][-1] = rangeDict["set" + str(i)][-1] + 1
                        plotArray[k] += 1

    plt.hist((plotArray))
    return rangeDict

# main:
image = cv2.imread("hamburger.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
levels = getHistogram(image, 128)
print(levels)
