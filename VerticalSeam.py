import numpy as np

def find_optimal_vertical_seam(cumulativeEnergyMap):
    # Get the dimensions of the cumulative energy map
    rows, cols = cumulativeEnergyMap.shape
    # Create a list to store the seam
    seam = []
    # Get the index of the minimum value in the last row
    minIndex = np.argmin(cumulativeEnergyMap[rows - 1, :])
    # Add the index to the seam list
    seam.append(minIndex)
    # Loop through the rows
    for i in range(rows - 1, 0, -1):
        # If the index is 0
        if minIndex == 0:
            # Get the index of the minimum value in the three pixels above
            req = np.argmin(cumulativeEnergyMap[i - 1, minIndex:minIndex + 2])
            # Add the index to the seam list
            minIndex = minIndex + req
            seam.append(minIndex)
        # If the index is the last column
        elif minIndex == cols - 1:
            # Get the index of the minimum value in the three pixels above
            req = np.argmin(cumulativeEnergyMap[i - 1, minIndex - 1:minIndex + 1])
            # Add the index to the seam list\
            minIndex = minIndex - 1 + req
            seam.append(minIndex)
        # If the index is in between
        else:
            # Get the index of the minimum value in the three pixels above
            req = np.argmin(cumulativeEnergyMap[i - 1, minIndex - 1:minIndex + 2])
            # Add the index to the seam list
            minIndex = minIndex - 1 + req
            seam.append(minIndex)
    # Reverse the seam list
    seam.reverse()
    # Return the seam list
    return seam