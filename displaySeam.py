import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def displaySeam(img, seam, type):
    # Read the image
    img = mpimg.imread(img)
    # Get the dimensions of the image
    rows, cols, _ = img.shape
    # Create a new figure
    plt.figure()
    # Display the image
    plt.imshow(img)
    # If the type is horizontal
    if type == 'HORIZONTAL':
        # Loop through the columns
        for i in range(cols):
            # Plot the seam
            plt.plot(i, seam[i], 'r.')
    # If the type is vertical
    elif type == 'VERTICAL':
        print(seam)
        # Loop through the rows
        for i in range(rows):
            # Plot the seam
            plt.plot(seam[i], i, 'r.')
    # Show the plot
    plt.show()