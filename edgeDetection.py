#Perform Edge Detection using Roberts Cross Gradient & Sobel Operators over an Image

import cv2
import math
import numpy as np

def robertCrossGradient(image):
	#Objective: Performing Robert Cross Gradient Edge Detection over an Image
	#Input: Original Image
	#Output: Resultant Image
	
	#Robert Cross Operator
	# x  0 1
	#	-1 0
	# y  1  0
	#	 0 -1
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Converting Image to Gray Scale
	resultant_image = image.copy()
	for i in range(0,image.shape[0]-1):
	    for j in range(0,image.shape[1]-1):
	        gx = image[i, j+1] - image[i+1, j]
	        gy = image[i, j] - image[i+1, j+1]
	        resultant_image[i, j] =  math.sqrt(gx*gx + gy*gy)	
	
	return resultant_image

def sobelOperator(image):
    #Objective: Performing Sobel Edge Detection over an Image
	#Input: Original Image
	#Output: Resultant Image
	
	#Sobel Operator
	
	# x -1 -2 -1
	#    0  0  0
	#    1  2  1
	
	#y  -1  0  1
	#   -2  0  2
	#   -1  0  1
	
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Converting Image to Gray Scale
	resultant_image = image.copy()
	
	#Applying Padding
	rows,cols = image.shape
	image = np.insert(image,0,0,axis=0) #top
	image = np.insert(image,rows+1,0,axis=0) #bottom
	image = np.insert(image,0,0,axis=1) #left
	image = np.insert(image,cols+1,0,axis=1) #right
	
	for i in range(1, image.shape[0]-1):
	    for j in range(1, image.shape[1]-1):
	        fx = image[i+1, j-1] + 2*image[i+1, j] + image[i+1, j+1] - image[i-1, j-1] - 2*image[i-1, j] - image[i+1, j-1]
	        fy = image[i-1, j+1] + 2*image[i, j+1] + image[i+1, j+1] - image[i-1, j-1] - 2*image[i, j-1] - image[i+1, j-1]
	        resultant_image[i-1, j-1] =  math.sqrt(fx*fx + fy*fy)
	
	return resultant_image

img = cv2.imread('image5.jpg')
output = sobelOperator(img)

cv2.imshow('image',output)
cv2.waitKey(0)
cv2.destroyAllWindows()
