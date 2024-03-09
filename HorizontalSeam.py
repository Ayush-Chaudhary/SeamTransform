import numpy as np

def find_optimal_horizontal_seam(cumulativeEnergyMap):
    # Get the dimensions of the cumulative energy map
    rows, cols = cumulativeEnergyMap.shape
    # Create a list to store the seam
    seam = []
    # Get the index of the minimum value in the last column
    minIndex = np.argmin(cumulativeEnergyMap[:, cols - 1])
    # Add the index to the seam list
    seam.append(minIndex)
    # Loop through the columns
    for i in range(cols - 1, 0, -1):
        # If the index is 0
        if minIndex == 0:
            # Get the index of the minimum value in the three pixels to the left
            req = np.argmin(cumulativeEnergyMap[minIndex:minIndex + 2, i - 1])
            # Add the index to the seam list
            minIndex = minIndex + req
            seam.append(minIndex)
        # If the index is the last row
        elif minIndex == rows - 1:
            # Get the index of the minimum value in the three pixels to the left
            req = np.argmin(cumulativeEnergyMap[minIndex - 1:minIndex + 1, i - 1])
            # Add the index to the seam list
            minIndex = minIndex - 1 + req
            seam.append(minIndex)
        # If the index is in between
        else:
            # Get the index of the minimum value in the three pixels to the left
            req = np.argmin(cumulativeEnergyMap[minIndex - 1:minIndex + 2, i - 1])
            # Add the index to the seam list
            minIndex = minIndex - 1 + req
            seam.append(minIndex)
    # Reverse the seam list
    seam.reverse()
    # Return the seam list
    return seam
