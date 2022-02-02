import cv2 as cv
import numpy as np

img = cv.imread('Photos/Frank.png')
cv.imshow('ocean',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# laplacian
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
# absolute 쓰는 이유: gradient를 취하면 negative value가 나오는데
# 픽셀이 positive value이므로 
# uint8은 image specific datatype..
cv.imshow('Laplacian', lap)

# sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1,0)
sobely = cv.Sobel(gray, cv.CV_64F, 0,1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('sobel X', sobelx)
cv.imshow('sobel y', sobely)
cv.imshow('sobel combined', combined_sobel)
# sobel을 advance cv에서 많이 사용하긴 함.

cv.waitKey(0)