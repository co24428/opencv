import cv2
import time
white_fname = './image/white.jpg'
# 1~9
fnum = 1

fname = f'./coffee_bean/coffee{fnum}.png'
output_resize_fname  = f'./coffee_bean/output/coffee{fnum}.png'
output_contour_fname = f'./coffee_bean/output/coffee{fnum}_contour.png'

white = cv2.imread(white_fname , cv2.IMREAD_COLOR) # 윤곽선 배경
src = cv2.imread(fname , cv2.IMREAD_COLOR) # 원본 이미지
src_resize = cv2.resize(src, dsize=(100, 100), interpolation=cv2.INTER_AREA) # resize
gray = cv2.cvtColor(src_resize, cv2.COLOR_RGB2GRAY)

ret, binary = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)

binary = cv2.bitwise_not(binary)
cv2.imshow("gray", gray)
cv2.imshow("binary", binary)

contours, hierachy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

max_iter = 0
max = 0
for i in range(len(contours)):
    if max < len(contours[i]):
        max = len(contours[i])
        max_iter = i
        
cv2.imwrite(output_resize_fname, src_resize)

cv2.drawContours(src_resize, [contours[max_iter]], 0, (0, 0, 255), 1)
cv2.imshow("src_resize", src_resize)
cv2.drawContours(white, [contours[max_iter]], 0, (0, 0, 255), 1)
cv2.imshow("white", white)

cv2.waitKey(0)
cv2.imwrite(output_contour_fname, white)

cv2.destroyAllWindows()
