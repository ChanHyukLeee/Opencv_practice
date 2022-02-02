import cv2 as cv
img = cv.imread('Photos/cats.jpg')

cv.imshow('cat', img)

# reduce noise -> lots of blurring technique
# Define kernel or window -> size(3,3) (5,5)...

#2d convolution filter
kernel = np.ones((5,5),np.float32)/25
fil = cv.filter2D(img, -1, kernel)


#Averaging
# surrounding pixel의 평균이 middle pixel값
average = cv.blur(img,(3,3))
cv.imshow('Average blur', average)
# kernel size 늘리면 더 blur

# Gaussian blur
# less blurring than average method and natural
# weight value 가 곱해짐
gauss = cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian blur', gauss)
 
# median blur
# more effective 
median = cv.medianBlur(img,3)
cv.imshow('median blur', median)

# bilateral blurring
#most effective,retain the edges in this image
bilateral = cv.bilateralFilter(img,5, 15, 50)
# sigma space 커지면 서로 영향 더 커짐
# 책으로 보완할 필요성
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)