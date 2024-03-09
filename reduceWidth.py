import numpy as np
from VerticalSeam import find_optimal_vertical_seam

def reduceWidth(im, energyImage):
    # Get the dimensions of the image
    rows, cols, _ = im.shape
    # Get the optimal vertical seam
    verticalSeam = find_optimal_vertical_seam(energyImage)
    # Create a new image
    reducedColorImage = np.zeros((rows, cols - 1, 3), dtype=np.uint8)
    # Create a new energy image
    reducedEnergyImage = np.zeros((rows, cols - 1), dtype=np.double)
    # Loop through the rows
    for i in range(rows):
        # Remove the seam from the image
        reducedColorImage[i, :, :] = np.delete(im[i, :, :], verticalSeam[i], 0)
    # Loop through the rows
    for i in range(rows):
        # Remove the seam from the energy image
        reducedEnergyImage[i, :] = np.delete(energyImage[i, :], verticalSeam[i], 0)
    # Return the reduced image and energy image
    return reducedColorImage, reducedEnergyImage, verticalSeam