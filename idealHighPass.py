import numpy as np

# The function takes two dimension inputs for the filter image;
# the third filter is D0, which defines the circle area of the High Pass Filter.
def idealHighPass(M, N, D0):
    # Initializing the filter with ones; since the filter is a complex function,
    # it has two channels, representing the real and imaginary parts:
    filter = np.ones((M, N, 2), dtype=np.float32)
    
    # Scanning through each pixel and calculating the distance of each pixel
    # to the image center. If the pixel is within D0, it is changed to 0:
    for i in range(M):
        for j in range(N):
            
            D = ((i - M/2)**2 + (j - N/2)**2)**(1/2)

            if D <= D0:
                filter[i][j] = 0

    return filter