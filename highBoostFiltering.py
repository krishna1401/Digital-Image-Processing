#Perform High-Boost Filtering over an Image
#High-Boost Filtering Formula
#resultant_pixel_value = A*original_pixel_value - blurred_pixel_value
#where A is the Boosting Factor

import cv2

def highBoostFiltering(image,boost_factor):
    #Objective: Performing High-Boost Filtering over an Image
    #Input: Original Image & Filtering Factor
    #Output: Resultant Image
    
    # Blur Kernel Matrix
    #   1/9 1/9 1/9
    #   1/9 1/9 1/9
    #   1/9 1/9 1/9
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Converting Image to Gray Scale
    resultant_image = image.copy()
    for i in range(1,image.shape[0]-1):
        for j in range(1,image.shape[1]-1):
            blur_factor = (image[i-1, j-1] + image[i-1, j] - image[i-1, j+1] + image[i, j-1] + image[i, j] + image[i, j+1] + image[i+1, j+1] + image[i+1, j] + image[i+1, j+1])/9
            resultant_image[i, j] = boost_factor*image[i, j] - blur_factor
            
    return resultant_image

img = cv2.imread('image2.jpg')
factor = input('Enter the value of Filter Factor for High-Boost Filtering : ')
output = highBoostFiltering(img, factor)

cv2.imshow('image',output)
cv2.waitKey(0)
cv2.destroyAllWindows()
