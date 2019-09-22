#Program to perform an Histogram Equalization on an Image

import cv2
import numpy as np
import matplotlib.pyplot as plt
import math


def histogramEqualization(image):
    #Objective: Display Intensity Histogram for an Image
    #Input: Original Image
    #Output: Return Equalized Image
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Converting Image to Gray Scale
    intensityFrequency = [0.0]*256
    height = image.shape[0]
    width = image.shape[1]
    no_of_pixels = height*width
    
    #Finding the Frequency of each Intensity Level in an Image
    for i in range(0, height):
        for j in range(0, width):
            intensityFrequency[image[i, j]] += 1.0
    
    #Probability of each Intensity Level
    for i in range(0,256):
        intensityFrequency[i] = intensityFrequency[i]/no_of_pixels
        
    #Mapping of Intensity Level to the Corresponding Resultant Intensity Level
    #Resultant Intensity Level = floor(Cumulative Frequency of an Intensity Level * (Maximum Level - 1) + 0.5)
    cumulativeIntensityFrequency = 0.0
    mappingIntensityLevel = [0]*256
    for i in range(0,256):
        cumulativeIntensityFrequency += intensityFrequency[i]
        mappingIntensityLevel[i] = math.floor(cumulativeIntensityFrequency * 255 + 0.5)
        
    print(mappingIntensityLevel)    
    #Creating a Resultant Image
    #Mapping Original Intensity Level with the Resultant Intensity Level
    resultant_image = image.copy()
    for i in range(0, height):
        for j in range(0, width):
            resultant_image[i ,j] = mappingIntensityLevel[image[i, j]]
    
    return resultant_image
    
img = cv2.imread('image2.jpg')
output = histogramEqualization(img)

cv2.imshow('image',output)
cv2.waitKey(0)
cv2.destroyAllWindows()
