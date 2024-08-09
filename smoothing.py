import cv2 as cv

img = cv.imread('images/spring-rolls-8135469_640.jpg')
cv.imshow('Spring Rolls',img)

# average blur
average = cv.blur(img,(3,3))
cv.imshow('Average Blur',average)

# gaussian blurr
guass = cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian Blur',guass) 

# median blur
median = cv.medianBlur(img,3)
cv.imshow('Median Blur',median)

# bilateral blur
bilateral = cv.bilateralFilter(img,5,50,15)
cv.imshow('Bilateral Filter',bilateral)

cv.waitKey(0)