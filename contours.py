import cv2 as cv
import numpy as np

# Read the image
img = cv.imread('images/spring-rolls-8135469_640.jpg')

# Check if the image was loaded properly
if img is None:
    print("Error: Image not found or cannot be opened.")
else:
    # Display the original image
    cv.imshow('Original Spring Rolls', img)
    
    # Convert the image to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    # Display the grayscale image
    cv.imshow('Grayscale Spring Rolls', gray)
    
    # Position the windows
    cv.moveWindow('Original Spring Rolls', 100, 100)
    cv.moveWindow('Grayscale Spring Rolls', 500, 100)
    
    blur = cv.GuassianBlur(gray,(5,5),cv.BORDER_DEFAULT)
    cv.imshow('Blur', blur)
    
    canny = cv.Canny(img,125,75)
    cv.imshow('Canny Edges', canny)
    
    blank = np.zeros(img.shape,dtype='uint8')
    cv.imshow('Blank', blank)
    
    ret, thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
    cv.imshow('Thresh', thresh)
    
    contours, hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
    print(f'{len(contours)} contour(s) found!')
    
    cv.drawContours(blank,contours,-1,(0,0,255),1)
    cv.imshow('Contour', blank)
    
    # Wait for a key press indefinitely
    cv.waitKey(0)
    
    # Destroy all windows
    cv.destroyAllWindows()


# img1 = cv.imread('images/normal.jpg')
# img2 = cv.imread('images/diabetic.jpg')

# i1 = cv.Canny(img1,100,100)
# cv.imshow('Normal',i1)


# i2 = cv.Canny(img2,100,100)
# cv.imshow('Diabetic',i2)
# # Wait for a key press indefinitely
# cv.waitKey(0)
    
#     # Destroy all windows
# cv.destroyAllWindows()