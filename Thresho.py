import cv2 as cv

img = cv.imread('Photos/Frank.png')
cv.imshow('ocean',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# simple thresholding
threshold, thresh = cv.threshold(gray,150,255, cv.THRESH_BINARY)
# THRESHOLD 못넘으면 ZERO
# threshold 높게 하면 많이 zero
cv.imshow('simple thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray,150,255, cv.THRESH_BINARY_INV)
cv.imshow('simple thresholded inverse', thresh_inv)
# 흑백이 반대로 바뀜

#Adaptive thersholding
# find the optimal value by itself
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,3)
# 11, 3 에 있는 값에 따라 threshold 달라짐
# mean외에도 gaussian도 가능
# adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,3)
cv.imshow('adaptive thresholded', adaptive_thresh)
cv.waitKey(0)