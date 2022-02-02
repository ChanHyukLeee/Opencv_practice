import cv2 as cv
import numpy as np

isDragging = False
x0, y0, w, h = -1, -1, -1, -1
blue ,red = (255,0,0), (0,0,255)

def onMouse(event, x,y,flags, param):
    global isDragging, x0, y0, img
    if event == cv.EVENT_FLAG_LBUTTONDOWN:
        isDragging = True
        x0 = x
        y0 = y
    elif event == cv.EVENT_MOUSEMOVE:
        if isDragging:
            img_draw = img.copy()
            cv.rectangle(img_draw, (x0,y0), (x,y), blue, 2)
            cv.imshow('img', img_draw)
    elif event == cv.EVENT_LBUTTONUP:
        if isDragging:
            isdragging = False
            w = x-x0
            h = y-y0
            print("x:%d, y:%d, w:%d, h:%d" % (x0, y0, w,h))
            if w > 0 and h >0 :
                img_draw = img.copy()
                cv.rectangle(img_draw, (x0, y0), (x,y), red, 2)
                cv.imshow('img', img_draw)
                roi = img[y0:y0+h, x0:x0+w]
                cv.imshow('cropped', roi)
                cv.moveWindow('cropped', 0,0)
                cv.imwrite('./cropped.jpg', roi)
                print("cropped.")
            else:
                cv.imshow('img',img)
                print("wrong")

img = cv.imread('Photos/Frank.png')
cv.imshow('img',img)
cv.setMouseCallback('img', onMouse)
cv.waitKey(0)
