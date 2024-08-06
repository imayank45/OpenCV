import cv2 as cv

img = cv.imread('images/spring-rolls-8135469_640.jpg')
cv.imshow('Spring Rolls', img)

# BGR to Gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('BGR to Gray scale', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('BGR to HSV', hsv)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('BGR to LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('BGR to RGB',rgb)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR',hsv_bgr)

# LAB TO BGR    
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB to BGR',lab_bgr)

cv.waitKey(0)