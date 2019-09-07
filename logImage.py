#Program to perform Log Transformation over an Image
#Log Transformation
#resultant_pixel = c * log(actual_pixel + 1)
#where c is a constant calculated as 
#c = 255/log(maximum_pixel_value + 1)

import cv2
import numpy as np

def logTranformationofImage(image):
    #Objective: Perform Log Transformation    
    #Input: Original Image
    #Output: Resultant Image
    
    maximum_pixel_value = np.max(image)
    height = image.shape[0]
    width = image.shape[1]
    
    c = 255 / np.log(maximum_pixel_value + 1)
    for i in range(0, height):
        for j in range(0, width):
            image[i, j] = c * np.log(image[i, j] + 1)
    return image
    
img = cv2.imread('image1.png')
output = logTranformationofImage(img)

cv2.imshow('image',output)
cv2.waitKey(0)
cv2.destroyAllWindows()

