import numpy as np
import math

# The function takes two dimension inputs for the filter image;
# the third filter is D0, which defines the circle area of the High Pass Filter;
def highGaussian(M, N, D0):
    # Initializing the filter with ones; since the filter is a complex function,
    # it has two channels, representing the real and imaginary parts;
    # the data type is float32, since the pixel will take floating point values,
    # between 0. and 1:
    filter = np.ones((M, N, 2), dtype=np.float32)
    
    # Scanning through each pixel and calculating the distance of each pixel
    # to the image center. After the distance is calculated, operation on line 20
    # will be applied.
    for i in range(M):
        for j in range(N):
            D = ((i - int(M/2))**2 + (j - int(N/2))**2)**(1/2)

            filter[i][j] = 1 - math.exp(-(D**2) / ((2)*D0**2))

    return filter