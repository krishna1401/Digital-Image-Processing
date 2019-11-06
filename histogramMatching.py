#Program to match the histogram on an input image with the target image

import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

def displayHistogram(image):
    intensityFrequency = [0]*256
    height = image.shape[0]
    width = image.shape[1]
    
    for i in range(0, height):
        for j in range(0, width):
            intensityFrequency[image[i, j]] += 1
    
    index = np.arange(0,256)
    plt.bar(index, intensityFrequency)
    plt.xlabel('Intensity Level')
    plt.ylabel('Frequency')
    plt.show()

def histogramMapping(image,target):
    #Objective: Display Intensity Histogram for an Image
    #Input: Original Image
    #Output: Return Equalized Image
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Converting Image to Gray Scale
    imageIntensityFrequency = [0.0]*256
    height_image = image.shape[0]
    width_image = image.shape[1]
    no_of_pixels_image = height_image*width_image
    
    target = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY) #Converting Target to Gray Scale
    targetIntensityFrequency = [0.0]*256
    height_target = target.shape[0]
    width_target = target.shape[1]
    no_of_pixels_target = height_target*width_target
    
        
    
    #Finding the Frequency of each Intensity Level in an Image
    for i in range(0, height_image):
        for j in range(0, width_image):
            imageIntensityFrequency[image[i, j]] += 1.0
    
    #Finding the Frequency of each Intensity Level in a Target
    for i in range(0, height_target):
        for j in range(0, width_target):
            targetIntensityFrequency[image[i, j]] += 1.0
    
    #Probability of each Intensity Level
    for i in range(0,256):
        imageIntensityFrequency[i] = imageIntensityFrequency[i]/no_of_pixels_image
        targetIntensityFrequency[i] = targetIntensityFrequency[i]/no_of_pixels_target
        
    #Cumulative Intensity of Target and Input Image
    imageCumulativeIntensity = [0.0]*256
    targetCumulativeIntensity = [0.0]*256
    
    imageCumulativeIntensity[0] = imageIntensityFrequency[0]
    targetCumulativeIntensity[0] = targetIntensityFrequency[0]
    for i in range(1,256):
        imageCumulativeIntensity[i] = imageIntensityFrequency[i] + imageCumulativeIntensity[i-1]
        targetCumulativeIntensity[i] = targetIntensityFrequency[i] + targetCumulativeIntensity[i-1]
        
    for i in range(0,256):
        #Setting Precision upto 2 decimal places
        imageCumulativeIntensity[i] = "{0:.2f}".format(imageCumulativeIntensity[i],2)
        targetCumulativeIntensity[i] = "{0:.2f}".format(targetCumulativeIntensity[i],2)

    mappingIntensityLevel = [0]*256
    for i in range(0,256):
        for j in range(0,256):
            #Make Changes
            if imageCumulativeIntensity[i] == targetCumulativeIntensity[j]:
                mappingIntensityLevel[i] = j
                break
        
    print(mappingIntensityLevel)    
    #Creating a Resultant Image
    #Mapping Original Intensity Level with the Resultant Intensity Level
    resultant_image = image.copy()
    for i in range(0, height_image):
        for j in range(0, width_image):
            resultant_image[i ,j] = mappingIntensityLevel[image[i, j]]

    #displayHistogram(image)
    #displayHistogram(target)
    #displayHistogram(resultant_image)

    return resultant_image

img = cv2.imread('image3.jpg')
tar = cv2.imread('image2.jpg')
output = histogramMapping(img,tar)

cv2.imshow('image',output)
cv2.waitKey(0)
cv2.destroyAllWindows()
