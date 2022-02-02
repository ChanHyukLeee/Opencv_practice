import cv2 as cv
import numpy as np

img = cv.imread('Photos/lady.jpg')
cv.imshow('Lady',img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

# reconstruct only one color channel
blue = cv.merge([b,blank,blank]) # blue channel 만 존재
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue', blue)
cv.imshow('GReen', green)
cv.imshow('Red', red)
# grayscale로 표현
# dark하면 little or no pixel
# white하면 concentration a lot


print(img.shape) # (427,640,3) : 3은 channel 수 뜻함
print(b.shape)  # (427, 640)으로 다 동일
print(g.shape)
print(r.shape)

#merge image
merged = cv.merge([b,g,r])
cv.imshow('merge', merged)


cv.waitKey(0)