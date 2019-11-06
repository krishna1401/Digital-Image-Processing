#Perform Unsharp Masking over an Image
#Unsharp Masking Formula
#resultant_pixel_value = original_pixel_value - blurred_pixel_value

import cv2

def unsharpMasking(image):
    #Objective: Performing Unsharp Masking over an Image
    #Input: Original Image
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
            mask = image[i, j] - blur_factor
            resultant_image[i, j] = image[i, j] + mask
            
    return resultant_image

img = cv2.imread('image2.jpg')
output = unsharpMasking(img)

cv2.imshow('image',output)
cv2.waitKey(0)
cv2.destroyAllWindows()
