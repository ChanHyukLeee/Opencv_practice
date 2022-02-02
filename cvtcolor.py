import cv2 as cv
# import matplotlib.pyplot as plt


img = cv.imread('Photos/park.jpg')
cv.imshow('Boston', img)

# plt.imshow(img)
# plt.show()

#BGR to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GRay',gray)

#BGR to HSV(human)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

# BGR to L*A*B
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

# BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)
# matplotlib은 RGB를 사용하므로
# matplotlib를 쓸 거면 이처럼 RGB로 먼저 변환 후 사용해야함
# color 뒤에만 바꾸면 다 convert가능

cv.waitKey(0)