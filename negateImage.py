#Program to create a negative of an Image

import cv2
import numpy as nm

def negateImage(image):
    #Objective: Negating an Image
    #Input: Original Image
    #Output: Negated Image

    height = image.shape[0]
    width = image.shape[1]
    
    for i in range(0, height):
        for j in range(0, width):
            R, B, G = image[i, j]
            #Updating Red Color
            R = 255 - R
            #Updating Blue Color
            B = 255 - B
            #Updating Green Color
            G = 255 - G
            
            image[i, j] = [R, B, G]
    return image
    
img = cv2.imread('image.jpeg')
output = negateImage(img)

cv2.imshow('image',output)
cv2.waitKey(0)
cv2.destroyAllWindows()

