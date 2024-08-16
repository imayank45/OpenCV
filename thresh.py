import cv2 as cv

img = cv.imread('images/spring-rolls-8135469_640.jpg')
cv.imshow('Spring Roll', img)

# gray scale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# simpel thresholding
threshold, thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('Simple', thresh)

threshold, thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresolded Inverse', thresh_inv)\

# adaptive thresholding
adaptive_threshold = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2 )
cv.imshow('Adaptive Threshold',adaptive_threshold)

cv.waitKey(0)