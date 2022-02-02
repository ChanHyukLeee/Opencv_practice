import cv2 as cv
import numpy as np

img= cv.imread()
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

corner = cv.cornerHarris(gray, 2, 3, 0.04)
#corner 검출
coord = np.where(corner> 0.1*corner.max())
coord = np.stack((coord[1], coord[0]), axis = -1)
# 최대값 10%의 좌표 

for x,y in coord:
	cv.circle(img, (x,y), 5, (0,255,0), 1, cv.LINE_AA)
# 원 그리기

corner_norm = cv.normalize(corner, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
# 영상표현하기 위해 0-255로 정규화

corner_norm = cv.cvtColor(corner_norm, cv.COLOR_GRAY2BGR)
merged = np.hstack((corner_norm, img))