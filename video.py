import cv2 as cv

capture = cv.VideoCapture('videos/dog.mp4')
# 0는 내 웹캠, 혹은 first camera 
while True:
    isTrue, frame = capture.read()
    # frame by frame 으로 
    cv.imshow('Video', frame)


    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    # while문을 벗어나야 하는데, waitkey가 20이고 letter D가 나오면 break

capture.release()
cv.destroyAllWindows()