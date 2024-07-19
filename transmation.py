import cv2 as cv
import numpy as np

img = cv.imread('images/spring-rolls-8135469_640.jpg')
cv.imshow('Spring Roll', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> Up
# x --> Right
# y --> Down

translated_img = translate(img, -100, 50)
cv.imshow('Translated Image', translated_img)


# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('rotated image', rotated)

rotated_rotated = rotate(rotated, -45)
cv.imshow('Rotated Rotated image', rotated_rotated)

cv.waitKey(0)