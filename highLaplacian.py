import numpy as np
from matplotlib import pyplot as plt
import math

# The function takes two dimension inputs for the filter image;
def highLaplacian(M, N):
    # Initializing the filter with ones; since the filter is a complex function,
    # it has two channels, representing the real and imaginary parts;
    # the data type is float32, since the pixels will take floating point values:
    filter = np.zeros((M, N, 2), dtype=np.float32)
    
    # Scanning through each pixel and calculating the negative of the sum of the
    # squares of the pixels (after centering them), and assigning the value to the corresponding pixel
    # in the filter:
    for i in range(M):
        for j in range(N):
            filter[i][j] = -4*(np.pi**2)*((i-M/2)**2 + (j-N/2)**2)

    return filter