#Perform Boolean operation (OR/AND) over two images

import cv2

def performAND(image1, image2):
    #Objective: Perform Boolean AND between 2 images
    #Input: Two Images
    #Output: Resultant Image
    
    if(image1.shape[0] == image2.shape[0] and image1.shape[1] == image2.shape[1]):
        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY) #Converting Image to Gray Scale
        image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY) #Converting Image to Gray Scale
        
        resultant_image = image1.copy() 
        for i in range(0,image1.shape[0]):
            for j in range(0,image1.shape[1]):
                resultant_image[i, j] = image1[i, j] and image2[i, j]
        
        return resultant_image
        
    else:
        print("Incompartible Size")
        system.exit();

def performOR(image1, image2):
    #Objective: Perform Boolean OR between 2 images
    #Input: Two Images
    #Output: Resultant Image
    
    if(image1.shape[0] == image2.shape[0] and image1.shape[1] == image2.shape[1]):
        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY) #Converting Image to Gray Scale
        image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY) #Converting Image to Gray Scale
        
        resultant_image = image1.copy()
        
        for i in range(0,image1.shape[0]):
            for j in range(0,image1.shape[1]):
                resultant_image[i, j] = image1[i, j] or image2[i, j]
        
        return resultant_image
        
    else:
        print("Incompartible Size")
        system.exit();
    

img1 = cv2.imread('image2.jpg')
img2 = cv2.imread('image4.jpg')

#AND Operation
output = performAND(img1,img2)
cv2.imshow('image',output)
cv2.waitKey(0)
cv2.destroyAllWindows()

#OR Operation
output = performOR(img1,img2)
cv2.imshow('image',output)
cv2.waitKey(0)
cv2.destroyAllWindows()
