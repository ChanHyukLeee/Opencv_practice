import cv2 as cv

img = cv.imread('Photos/cat.jpg')


def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    # 1은 width, 0은 height 알기 float를 int로
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)
    # resize the frame in particular dimension

# def changeRes(width, height):
#     # livevideo만 
#     capture.set(3, width)
#     capture.set(4, height)




    
resized_image = rescaleFrame(img)
cv.imshow('cat',resized_image)
cv.waitKey(0)
# capture = cv.VideoCapture('videos/dog.mp4')

# while True:
#     isTrue, frame = capture.read()

#     frame_resized = rescaleFrame(frame)
#     cv.imshow('Video', frame)
#     cv.imshow('Video Resized', frame_resized)
    

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
 

# capture.release()
# cv.destroyAllWindows()