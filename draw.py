import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')
# zeros(height, width, number of color channel)
cv.imshow('Blank', blank)
# blank space

#1. paint the image
#blank[:] = 0, 255, 0 
# BGR, overall
blank[200:400, 300:400] = 0, 0, 255 
cv.imshow('Green', blank)

#2. draw rectangle
# cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)
# 함수보면 되고, 채워지지 않음 채우려면: thickness = cv.FILLED
cv.rectangle(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2),(0,255,0),thickness=-1)
# 정확히 반
cv.imshow('Rectangle', blank)

#3. draw circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
# 함수 잘 맞춰쓰면 됨, 채우려면 thickness = -1
cv.imshow('circle', blank)

#4. draw a line 
cv.line(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2),(255,255,255),thickness=3)
cv.imshow('line', blank)

#5. write text
cv.putText(blank,'hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0 ,(225,0,0), 2)
cv.imshow('text', blank)

cv.waitKey(0)