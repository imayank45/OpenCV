import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image with the certain color

# blank[:] = 0,255,0
# cv.imshow('Green',blank)

# blank[:] = 0,0,255
# cv.imshow('Red',blank)

# blank[:] = 255,0,0
# cv.imshow('Blue',blank)

# blank[200:300, 300:400] = 0,255,0
# cv.imshow('Green',blank)

# 2. Draw a rectangle
# cv.rectangle(blank, (0,0), (400,300), (0,255,0), thickness=-1)
# cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=-1)
# cv.imshow('Rectangle',blank)

# # 3. Draw a circle
# cv.circle(blank, (250,250), 40, (0,0,255), thickness=9)
# cv.imshow('Circle',blank)

# # 4. Draw a line
# cv.line(blank, (0,0), (400,300), (255,255,255), thickness=6)
# cv.imshow('Line',blank)

# 5. Write text on image
cv.putText(blank, 'Hello, world', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text',blank)

cv.waitKey(0)