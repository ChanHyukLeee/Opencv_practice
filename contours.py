import cv2 as cv
import numpy as np
img = cv.imread('Photos/cat.jpg')
cv.imshow('original', img)
cv.waitKey(0)

img2 = img.copy()
img_gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
img_gray = cv.GaussianBlur(img_gray,(3,3),0)
img_gray = cv.Canny(img_gray,75,200)
draw = img_gray.copy()
cv.imshow('canny',img_gray)
cv.waitKey(0)

cnts,b = cv.findContours(draw,cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(draw, cnts, -1, (0,255,0))
cv.imshow('drawcontour',draw)
cv.waitKey(0)

cnts = sorted(cnts, key= cv.contourArea, reverse= True)[:5]
for c in cnts:
    peri = cv.arcLength(c, True)
    vertices = cv.approxPolyDP(c, 0.02*peri, True)
    if len(vertices) ==4:
        break
pts = vertices.reshape(4, 2)
for x,y, in pts:
    cv.circle(draw, (x,y), 10 ,(0,255,0), -1)
cv.imshow('contourcircle', draw)
cv.waitKey(0)
merged = np.hstack((img,draw))