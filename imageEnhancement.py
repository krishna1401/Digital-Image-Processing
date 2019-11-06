#Program to perform Image Enhancement using Subtraction & Averaging technique

import cv2

def performSubtraction(image1, image2):
    #Objective: Perform subtraction of 2 images
    #Input: Two Images
    #Output: Resultant Image
    
    if(image1.shape[0] == image2.shape[0] and image1.shape[1] == image2.shape[1]):
        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY) #Converting Image to Gray Scale
        image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY) #Converting Image to Gray Scale
        
        resultant_image = image1.copy() 
        for i in range(0,image1.shape[0]):
            for j in range(0,image1.shape[1]):
                resultant_image[i, j] = abs(image1[i, j] - image2[i, j])
        return resultant_image
        
    else:
        print("Incompartible Size")
        system.exit();
        
def performAverage(image1, image2):
    #Objective: Perform subtraction of 2 images
    #Input: Two Images
    #Output: Resultant Image
    
    if(image1.shape[0] == image2.shape[0] and image1.shape[1] == image2.shape[1]):
        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY) #Converting Image to Gray Scale
        image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY) #Converting Image to Gray Scale
        
        resultant_image = image1.copy() 
        for i in range(0,image1.shape[0]):
            for j in range(0,image1.shape[1]):
                resultant_image[i, j] = (image1[i, j] + image2[i, j])/2
        return resultant_image
        
    else:
        print("Incompartible Size")
        system.exit();
        
        
img1 = cv2.imread('image2.jpg')
img2 = cv2.imread('image4.jpg')

#Image Subtraction
output = performSubtraction(img1,img2)
cv2.imshow('image',output)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Image Averaging
#output = performAverage(img1,img2)
#cv2.imshow('image',output)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
