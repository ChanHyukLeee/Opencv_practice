import numpy as np
import cv2 as cv

blank = np.zeros((400,400),dtype='uint8')

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370), 255,-1)
circle = cv.circle(blank.copy(),(200,200),200, 255, -1)

# cv.imshow("rectangle",rectangle)
# cv.imshow("circle", circle)

# bitwise and : intersecting region
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("and", bitwise_and)
# 겹친모양

#bitwise or : non-intersecting and intersecting region
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("or", bitwise_or)
# 둘다 합친모양

#bitwise xor : non-intersecting region
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("xor", bitwise_xor)

#bitwise not
bitwise_not = cv.bitwise_not(rectangle, circle)
cv.imshow("not", bitwise_not)


cv.waitKey(0)