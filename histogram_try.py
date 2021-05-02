import cv2
import numpy as np
from collections import defaultdict

def getHistogram(bin):  

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
            rangeDict["set" + str(i)].append(start + i)

        # When 255 is reached in the dictionary, loop will terminate:
        if rangeDict["set" + str(i)][-1] == 255:
            break

        else:
            # Assigning the greatest value in the most recently added key to the start:
            start = rangeDict["set" + str(i)][-1] 
            # Assigning start, plus the increment
            stop = start + increment
            # Initializing the next key:
            rangeDict["set" + str(i + 1)] = []
    # Printing the dictionary for checking:
    print(rangeDict)

# main:
getHistogram(128)
