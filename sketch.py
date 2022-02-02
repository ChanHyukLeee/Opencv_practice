import cv2 as cv
import numpy as np
img = cv.imread('Faces/val/madonna/1.jpg')

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_gray = cv.GaussianBlur(img_gray,(3,3),0,cv.INTER_LINEAR)
edges = cv.Laplacian(img_gray, -1, None, 5)

ret, sketch = cv.threshold(edges, 70 ,255, cv.THRESH_BINARY_INV)
kernel = cv.getStructuringElement(cv.MORPH_CROSS, (3,3))
sketch = cv.erode(sketch, kernel)

sketch = cv.medianBlur(sketch,5)
img_sketch = cv.cvtColor(sketch, cv.COLOR_GRAY2BGR)

cv.imshow('img', img_sketch)
cv.waitKey(0)
