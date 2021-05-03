import cv2
import numpy as np
import matplotlib.pyplot as plt

import os

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
    print("Creating the histogram...")
    
    while True:
        # Creating the array which will keep the sets of pixel values according to the bin:
        for i in range(start, stop):
            arrayToAppend = np.arange(start, stop, 1).tolist()

        # Creating a new key in the dictionary and assigning the most recent set values to it:
        rangeDict["set" + str(int(start/increment))] = arrayToAppend

        # If the most recently added set has 255 in it, that means we completed creating our set:
        if rangeDict["set" + str(int(start/increment))][-1] == 255:
            break
        
        # We are assigning one more of the most recently added set value as the start,
        # and adding increment to it before assigning to stop:
        else:
            start = rangeDict["set" + str(int(start/increment))][-1] + 1
            stop = start + increment

    # Initializing the plotArray which is going to consist of the frequency values of each set:
    plotArray = np.zeros((bin,), dtype=int)
    # Creating the x axis of the histogram, according to the bin input:
    xAxes = list(range(bin))

    # Evaluating which set each pixel in the image belongs to,
    # and then increasing frequency value of the corresponding set by 1:
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for k in range(len(rangeDict)):
                if image[i][j] in rangeDict["set" + str(k)]:
                    plotArray[k] += 1
                    continue
        # Since operation takes some time, process percentage is going to be printed out:
        #percent = int(i / image.shape[0] * 100)
        #print(str(percent) + "% completed.")
        #os.system('cls')

    # Creating the histogram using a bar array:
    plt.bar(xAxes, plotArray, width=1.0)
    plt.xlabel('Pixels according to the bin value')
    plt.ylabel('Frequency')
    plt.show()
    # Returning the plotArray:
    return plotArray

# main:
image = cv2.imread("algo_t.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
levels = getHistogram(image, 256)
print(levels)
#print(levels)
plt.hist(image.ravel(),256,[0,256]); plt.show()
