def cumulative_minimum_energy_map(energyImage, seamDirection):
    # Get the dimensions of the energy image
    rows, cols = energyImage.shape
    # Create a cumulative energy map
    cumulativeEnergyMap = energyImage.copy().astype('float64')
    # If the seam direction is horizontal
    if seamDirection == 'VERTICAL':
        # Loop through the rows
        for i in range(1, rows):
            # Loop through the columns
            for j in range(0, cols):
                # If the column is 0
                if j == 0:
                    # Add the minimum of the three pixels above
                    cumulativeEnergyMap[i, j] += min(cumulativeEnergyMap[i - 1, j], cumulativeEnergyMap[i - 1, j + 1])
                # If the column is the last column
                elif j == cols - 1:
                    # Add the minimum of the three pixels above
                    cumulativeEnergyMap[i, j] += min(cumulativeEnergyMap[i - 1, j - 1], cumulativeEnergyMap[i - 1, j])
                # If the column is in between
                else:
                    # Add the minimum of the three pixels above
                    cumulativeEnergyMap[i, j] += min(cumulativeEnergyMap[i - 1, j - 1], cumulativeEnergyMap[i - 1, j], cumulativeEnergyMap[i - 1, j + 1])
    # If the seam direction is vertical
    elif seamDirection == 'HORIZONTAL':
        # Loop through the columns
        for j in range(1, cols):
            # Loop through the rows
            for i in range(0, rows):
                # If the row is 0
                if i == 0:
                    # Add the minimum of the three pixels to the left
                    cumulativeEnergyMap[i, j] += min(cumulativeEnergyMap[i, j - 1], cumulativeEnergyMap[i + 1, j - 1])
                # If the row is the last row
                elif i == rows - 1:
                    # Add the minimum of the three pixels to the left
                    cumulativeEnergyMap[i, j] += min(cumulativeEnergyMap[i - 1, j - 1], cumulativeEnergyMap[i, j - 1])
                # If the row is in between
                else:
                    # Add the minimum of the three pixels to the left
                    cumulativeEnergyMap[i, j] += min(cumulativeEnergyMap[i - 1, j - 1], cumulativeEnergyMap[i, j - 1], cumulativeEnergyMap[i + 1, j - 1])
    # Return the cumulative energy map
    return cumulativeEnergyMap