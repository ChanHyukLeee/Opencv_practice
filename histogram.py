import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Photos/lady.jpg')
cv.imshow('lady', img)

blank = np.zeros(img.shape[:2], dtype= 'uint8')

#convert grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#masking
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100,255,-1)
masked = cv.bitwise_and(gray,gray,mask=mask)
cv.imshow('mask', masked)

# gray_hist = cv.calcHist([gray], [0],mask, [256], [0,256])
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel("Bins")
# plt.ylabel('# of labels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# color histogram
plt.figure()
plt.title('COLOR Histogram')
plt.xlabel("Bins")
plt.ylabel('# of labels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    # enumerate 칼러 열거
    hist = cv.calcHist([img], [i], masked, [250], [0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()



cv.waitKey(0)