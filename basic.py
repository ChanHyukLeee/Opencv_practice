import cv2 as cv
img = cv.imread('Photos/park.jpg')

cv.imshow('park', img)

#1 converting to grayscale,  흑백으로 변함 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

#2 Blur : noise를 reduce
# gaussian blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT )
# two by two tuple, kernel size = odd number
# kernel (3,3) -> (7,7) increase 하면 more blur
# cv.imshow('blur',blur )

#3 edge cascade
# find the edge // canny edge detector
canny = cv.Canny(img,125,175)
# edge 많음, edge를 줄이고 싶다면 img 대신 blur 사용
# canny = cv.Canny(blur,125,175)
# cv.imshow('Canny_edge', canny )

#4. dilate the image : canny edge
dilated = cv.dilate(canny, (7,7), iterations=3)
# iteration을 3으로 늘리면 더 thick해짐
# cv.imshow('dilated',dilated)

#5. eroding
eroded = cv.erode(dilated, (3,3), iterations= 1)
# cv.imshow('eroded', eroded)

#6 resize
resized = cv.resize(img, (500,500))
# 뒤에 interpolation = 에 따라 결과가 바뀜 
# cv.INTER_LINEAR: 영상확장, 4개 픽셀, 효용성 좋음
# cv.INTER_CUBIC : 영상확장, 16개 픽셀, 느리지만 퀄리티 더 좋음
# cv.INTER_AREA : 영상축소
# cv.imshow('resize',resized)

#7 cropping : image = array니깐 -> array slicing 
cropped = img[50:200, 200:400]
cv.imshow('cropped',cropped)

cv.waitKey(0)