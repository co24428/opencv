import cv2
import time
white_fname = './image/white.jpg'

fname = './image/coffee_resize.png'

white = cv2.imread(white_fname , cv2.IMREAD_COLOR) # 윤곽선 배경
src = cv2.imread(fname , cv2.IMREAD_COLOR) # 원본 이미지
gray = cv2.imread(fname, cv2.IMREAD_GRAYSCALE) # 1채널로 변경

ret, binary = cv2.threshold(gray, 194, 255, cv2.THRESH_BINARY)

binary = cv2.bitwise_not(binary)
cv2.imshow("src", src)
cv2.imshow("gray", gray)
cv2.imshow("binary", binary)

contours, hierachy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

max_iter = 0
max = 0
for i in range(len(contours)):
    if max < len(contours[i]):
        max = len(contours[i])
        max_iter = i
        
cv2.drawContours(src, [contours[max_iter]], 0, (0, 0, 255), 1)
cv2.imshow("src", src)
cv2.drawContours(white, [contours[max_iter]], 0, (0, 0, 255), 1)
cv2.imshow("white", white)

cv2.waitKey(0)
cv2.imwrite('./output/white.png', white)

cv2.destroyAllWindows()
