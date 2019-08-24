#Program to perform Power Law Transformation over an Image
#Power Law Transformation
#resultant_pixel = c * pixel_value^gamma
#where c is a constant calculated as 
#c = 255/log(maximum_pixel_value + 1)
    
import cv2
import numpy as np

def powerLawTranformationofImage(image, gamma):
    #Objective: Power Law Tranformation of an Image
    #Input: Original Image and Gamma Value
    #Output: Resultant Image    
    
    maximum_pixel_value = np.max(image)
    h = image.shape[0]
    w = image.shape[1]
    
    c = 255 / np.log(maximum_pixel_value + 1)
    for i in range(0, h):
        for j in range(0, w):
            image[i, j] = c * np.power(image[i, j], gamma)
    return image
    
img = cv2.imread('image.jpeg')
gamma = input('Enter the value of Gamma : ')
output = powerLawTranformationofImage(img,gamma)

cv2.imshow('image',output)
cv2.waitKey(0)
cv2.destroyAllWindows()

