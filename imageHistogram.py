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

    # If the bin input is 256, a different algorithm, which does not require an additional loop
    # for iterating through the dictionary will be used, in order to speed up the code:
    if bin == 256:
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                # Following line will return the key name, such as "set167":
                index = list(rangeDict.keys())[list(rangeDict.values()).index(image[i][j])]
                # Using split method to split the key name into two, such as -> ["set", "167"],
                # and then taking the second element to get the pixel intensity number:
                index = int(str(index.split("t")[1]))
                # Increasing the corresponding pixel intensity number, according to the match: 
                plotArray[index] += 1
                
    # If the bin input is different than 256, a less efficient algorithm which requires
    # iterating through the dictionary with a for loop will be used:
    else:
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                for k in range(len(rangeDict)):
                    # If the pixel value is between the max. and minimum value in the set, we find the match,
                    # and increase the corresponding intensity value by 1:
                    if image[i][j] <= max(rangeDict["set" + str(k)]) and image[i][j] >= min(rangeDict["set" + str(k)]):
                        plotArray[k] += 1
                        continue

    # Creating the histogram using a bar array:
    plt.bar(xAxes, plotArray, width=1.0)
    plt.xlabel('Pixels according to the bin value')
    plt.ylabel('Frequency')
    plt.show()
    # Returning the plotArray which contains the frequency of each intensity level:
    return plotArray
