import cv2 as cv
import numpy as np
img = cv.imread('data/trouble.jpg')
img = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
img = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('img',img)
cv.waitKey(0)