#imports
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from CumulativeEnergyMap import cumulative_minimum_energy_map
from reduceHeight import reduceHeight
from EnergyImage import getEnergy
from displaySeam import displaySeam

# Load a color input image called inputSeamCarvingPrague.jpg
img_path1 = 'Images\extra1.jpg'
img_path2 = 'Images\extra2.jpg'
img_path3 = 'Images\extra3.jpg'
img1 = mpimg.imread(img_path1)
img1 = mpimg.imread(img_path2)
img1 = mpimg.imread(img_path3)
energyImage = getEnergy(img1)

# Reduces the width of the image by 100 pixels using the above functions.
for i in range(100):
    energyImage = cumulative_minimum_energy_map(energyImage, 'HORIZONTAL')
    img1, energyImage, seam = reduceHeight(img1, energyImage)

# Saves the resulting image as outputReduceWidth Prague.png
# plt.imsave('Images\ReduceHeightextra1.png', img1)
# plt.imsave('Images\ReduceHeightextra2.png', img1)
plt.imsave('Images\ReduceHeightextra3.png', img1)

# # Reduces the height of the image by 100 pixels using the above functions.
# for i in range(100):
#     energyImage2 = cumulative_minimum_energy_map(energyImage2, 'HORIZONTAL')
#     img2, energyImage2, seam = reduceHeight(img2, energyImage2)

# # Saves the resulting image as outputReduceHeight Mall.png
# plt.imsave('ReduceHeightMall.png', img2)
