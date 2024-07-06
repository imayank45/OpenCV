import cv2 as cv

img = cv.imread('images/orange-parrots-8608540.jpg')
cv.imshow('Cat',img)

def rescale_frame(frame, scale=0.25):
    
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescale_frame(img)
cv.imshow('Image Resized', resized_image)

capture = cv.VideoCapture('videos/213616_tiny.mp4')

while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescale_frame(frame)
    
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)
    
    if cv.waitKey(25) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()