#Program to add a User enter Value to each colour Code of the Image

import cv2
import numpy as nm

def addValueToPixel(image, value):
    #Objective: Add Value to each Pixel of an Image
    #Input: Original Image and Value
    #Output: Resultant Image
    
    height = image.shape[0]
    width = image.shape[1]
    
    for i in range(0, height):
        for j in range(0, width):
            R, B, G = image[i, j]
            #Updating Red Color
            R += value
            R = R if R <= 255 else R-255
            #Updating Blue Color
            B += value
            B = B if B <= 255 else B-255
            #Updating Green Color
            G += value
            G = G if G <= 255 else G-255
            
            image[i, j] = [R, B, G]
    return image
    
img = cv2.imread('image.jpeg')
value = input('Enter the Value to be added to Each Pixel : ')
output = addValueToPixel(img,value)

cv2.imshow('image',output)
cv2.waitKey(0)
cv2.destroyAllWindows()

