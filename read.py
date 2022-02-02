import cv2 as cv

#img = cv.imread('Photos/cat_large.jpg')
# 사진 크기 따라 window열었을떄 달라짐
# dimension image > monitor image -> 확대
# Need resize
#cv.imshow('Cat', img)
#
# 
# 
capture = cv.VideoCapture('videos/dog.mp4')
# 0는 내 웹캠, 혹은 first camera 
while True:
    isTrue, frame = capture.read()
    # frame by frame 으로 
    cv.imshow('Video', frame)


    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    # while문을 벗어나야 하는데, waitkey가 20이고 letter D가 나오면 break
    # frame 없으면 break

capture.release()
cv.destroyAllWindows()
