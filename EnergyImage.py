import numpy as np
import scipy as sp
import cv2
import matplotlib.pyplot as plt

# def image_gradient_x_axis(gray_image):
#     H = np.array([[1, -1]])
#     gradient_x_axis = sp.ndimage.convolve(gray_image, H, cval=0, mode='constant')
#     return gradient_x_axis

# def image_gradient_y_axis(gray_image):
#     H = np.array([[1], [-1]])
#     gradient_y_axis = sp.ndimage.convolve(gray_image, H, cval=0, mode='constant')
#     return gradient_y_axis

# def getEnergy(im):
#     #Input im: Image with MxNx3 dimensions
#     #Output: Return 2D energy matrix of size MxN
#     gray_image = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#     gradient_x_axis = image_gradient_x_axis(gray_image)
#     gradient_y_axis = image_gradient_y_axis(gray_image)
#     return np.abs(gradient_x_axis) + np.abs(gradient_y_axis)


def getEnergy(im):
    #Input im: Image with MxNx3 dimensions
    #Output: Return 2D energy matrix of size MxN
    gray_image = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    gradient_x_axis = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    gradient_y_axis = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
    return np.abs(gradient_x_axis) + np.abs(gradient_y_axis)
