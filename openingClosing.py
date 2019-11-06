#Perform opening and closing of an Image

import cv2
from erosion import erosion
from dilation import dilation

def openingImage(img):
    #Objective: Performing Opening over an Image
    #Input: Original Image
    #Output: Resultant Image
    
    #First Erosion then Dilation
    image = erosion(img)
    image = cv2.cvtColor(image,cv2.COLOR_GRAY2RGB) #Converting Image back to RBG
    resultant_image = dilation(image)
    
    return resultant_image

def closingImage(img):
    #Objective: Performing Closing over an Image
    #Input: Original Image
    #Output: Resultant Image
    
    #First Dilation then Erosion
    image = dilation(img)
    image = cv2.cvtColor(image,cv2.COLOR_GRAY2RGB) #Converting Image back to RBG
    resultant_image = erosion(image)
    
    return resultant_image


img = cv2.imread('image6.jpg')
output = closingImage(img)

cv2.imshow('image',output)
cv2.waitKey(0)
cv2.destroyAllWindows()
