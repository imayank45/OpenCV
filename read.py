import cv2 as cv

# Reading images

# img = cv.imread('images//spring-rolls-8135469_640.jpg')

# cv.imshow('Spring Rolls',img)

# Reading videos

capture = cv.VideoCapture('videos/213616_tiny.mp4')

while True:
    isTrue, frame = capture.read()
    
    cv.imshow('Video',frame)
    
    if cv.waitKey(25) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()

