#Program to create an Histogram of Intensity for an Image

import cv2
import numpy as np
import matplotlib.pyplot as plt

def displayHistogram(image):
    #Objective: Display Intensity Histogram for an Image
    #Input: Original Image
    #Output:
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Converting Image to Gray Scale
    intensityFrequency = [0]*256
    height = image.shape[0]
    width = image.shape[1]
    
    for i in range(0, height):
        for j in range(0, width):
            intensityFrequency[image[i, j]] += 1
    
    for i in range(0,255):
        print(intensityFrequency[i])
    
img = cv2.imread('image.jpeg')
displayHistogram(img)
