#imports
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from CumulativeEnergyMap import cumulative_minimum_energy_map
from reduceWidth import reduceWidth
from EnergyImage import getEnergy
from displaySeam import displaySeam

# Load a color input image called inputSeamCarvingPrague.jpg
img_path1 = 'Images\extra1.jpg'
img_path2 = 'Images\extra2.jpg'
img_path3 = 'Images\extra3.jpg'
img_path4 = 'Images\extra4.jpg'
img1 = mpimg.imread(img_path1)
img1 = mpimg.imread(img_path2)
img1 = mpimg.imread(img_path3)
img1 = mpimg.imread(img_path4)
energyImage = getEnergy(img1)

# Reduces the width of the image by 100 pixels using the above functions.
for i in range(30):
    energyImage = cumulative_minimum_energy_map(energyImage, 'VERTICAL')
    img1, energyImage, seam = reduceWidth(img1, energyImage)

# Saves the resulting image as outputReduceWidth Prague.png
# plt.imsave('Images\ReduceWidthextra1.png', img1)
# plt.imsave('Images\ReduceWidthextra2.png', img1)
plt.imsave('Images\ReduceWidthextra4.png', img1)

# # Reduces the height of the image by 100 pixels using the above functions.
# for i in range(100):
#     energyImage2 = cumulative_minimum_energy_map(energyImage2, 'VERTICAL')
#     img2, energyImage2, seam = reduceWidth(img2, energyImage2)

# # Saves the resulting image as outputReduceHeight Mall.png
# plt.imsave('ReduceWidthMall.png', img2)
