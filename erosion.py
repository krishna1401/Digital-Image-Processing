#Perform Erosion of an Image

import cv2
import numpy as np

def checkErosion(element_set):
    condition = True
    for i in range(len(element_set)):
        for j in range(len(element_set[0])):
            if(element_set[i][j] == 0):
                condition = False
                break
    
    return condition

def erosion(image):
	#Objection: Perform Erosion over an Image
	#Input: Original Image
	#Output: Resultant Image
	
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Converting Image to Gray Scale
	resultant_image = image.copy()
	
	#Applying Padding
	rows,cols = image.shape
	image = np.insert(image,0,0,axis=0) #top
	image = np.insert(image,rows+1,0,axis=0) #bottom
	image = np.insert(image,0,0,axis=1) #left
	image = np.insert(image,cols+1,0,axis=1) #right
	
	for i in range(1,image.shape[0]-1):
	    for j in range(1,image.shape[1]-1):
	        element_set = [
	            [image[i-1, j-1], image[i-1, j], image[i-1, j+1]],
	            [image[i, j-1], image[i, j], image[i, j+1]],
	            [image[i+1, j-1], image[i+1, j], image[i+1, j+1]]
	        ]
	        if checkErosion(element_set) == False:
	            resultant_image[i-1, j-1] = 0
	
	return resultant_image

'''    
img = cv2.imread('image6.jpg')
output = erosion(img)

cv2.imshow('image',output)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
