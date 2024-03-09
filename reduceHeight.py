import numpy as np
from HorizontalSeam import find_optimal_horizontal_seam

def reduceHeight(im, energyImage):
    # Get the dimensions of the image
    rows, cols, _ = im.shape
    # Get the optimal vertical seam
    horizontalSeam = find_optimal_horizontal_seam(energyImage)
    # Create a new image
    reducedColorImage = np.zeros((rows - 1, cols, 3), dtype=np.uint8)
    # Create a new energy image
    reducedEnergyImage = np.zeros((rows - 1, cols), dtype=np.double)
    # Loop through the columns
    for i in range(cols):
        # Remove the seam from the image
        reducedColorImage[:, i, :] = np.delete(im[:, i, :], horizontalSeam[i], 0)
    # Loop through the columns
    for i in range(cols):
        # Remove the seam from the energy image
        reducedEnergyImage[:, i] = np.delete(energyImage[:, i], horizontalSeam[i], 0)
    # Return the reduced image and energy image
    return reducedColorImage, reducedEnergyImage, horizontalSeam