#Perform Laplacian Filtering on a Image

import cv2

def positiveLaplacianFilter(image):
    #Objective: Performing second order laplacian derivative over an image
    #Input: Original Image
    #Output: Filtered Image
    
    #   Positive Laplacian Filter
    #   0    1    0
    #   1   -4    1
    #   0    1    0
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Converting Image to Gray Scale
    resultant_image = image.copy()
    
    for i in range(1,image.shape[0]-1):
        for j in range(1,image.shape[1]-1):
            filter_over_i = image[i+1, j] + image[i-1, j] - 2*image[i, j]
            filter_over_j = image[i, j+1] + image[i, j-1] - 2*image[i, j]
            resultant_image[i, j] = filter_over_i + filter_over_j
            print(resultant_image[i, j])
    
    return resultant_image

def negativeLaplacianFilter(image):
    #Objective: Performing second order laplacian derivative over an image
    #Input: Original Image
    #Output: Filtered Image
    
    #   Negative Laplacian Filter
    #    0    -1     0
    #   -1     4    -1
    #    0    -1     0
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Converting Image to Gray Scale
    resultant_image = image.copy()
    
    for i in range(1,image.shape[0]-1):
        for j in range(1,image.shape[1]-1):
            filter_over_i = 2*image[i, j] - image[i+1, j] - image[i-1, j]
            filter_over_j = 2*image[i, j] - image[i, j+1] - image[i, j-1]
            resultant_image[i, j] = filter_over_i + filter_over_j
            print(resultant_image[i, j])
    
    return resultant_image

    
img = cv2.imread('image2.jpg')
output = positiveLaplacianFilter(img)

cv2.imshow('image',output)
cv2.waitKey(0)
cv2.destroyAllWindows()
