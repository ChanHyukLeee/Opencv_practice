import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_detect(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x,y,w,h) in faces:
        cropped = gray[x:x+w, y:y+h]
    return cropped

img = cv.imread('data/chanhyuk.jpg')
cropped = face_detect(img)
cv.imshow('lady', cropped)
cv.waitKey(0)