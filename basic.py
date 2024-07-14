import cv2 as cv

img = cv.imread('images/spring-rolls-8135469_640.jpg')
cv.imshow('Spring Roll', img)

# Converting to gray scale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# # Bluring an image
# blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# # Edge cascade
# canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny',canny)

# canny_blurr = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Blur',canny_blurr)

# # Dilated image
# dilated = cv.dilate(canny, (7,7), iterations=2)
# cv.imshow('Dilated Image', dilated)

# # Erode image
# eroded = cv.erode(dilated, (3,3), iterations=1)
# cv.imshow('Erode Image', eroded)

# Cropped image
cropped = img[50:200, 200:400]
cv.imshow('Cropped Image', cropped)

cv.waitKey(0)