import cv2
import time
white_fname = './image/white.jpg'

fname = './image/coffee_b_resize.jpg'
# fname = './image/insect_damage_resize.jpg'
# fname = './image/insect_damage.jpg'
# fname = './image/coffee.png'
# fname = './image/cap.png'
# fname = './image/man.jpg'

# 1. 
# 윤곽선 검출 => 하얀색을 검출!
# 배경은 검은색, 물체는 하얀색으로 변형해야함
# 이진화 처리 후 반전시켜서 물체를 하얀색을 띄게 한다.

# 코드 안먹어서 분할시킴
# src = cv2.imread(fname , cv2.IMREAD_COLOR)
# gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)

# insert
white = cv2.imread(white_fname , cv2.IMREAD_COLOR)
src = cv2.imread(fname , cv2.IMREAD_COLOR)
gray = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)

# ret, binary = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY)
# ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
# ret, binary = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)
ret, binary = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)
binary = cv2.bitwise_not(binary)
cv2.imshow("src", src)
cv2.imshow("gray", gray)
cv2.imshow("binary", binary)

# 2. 
# cv2.findContours로 이진화 이미지에서 윤곽선을 검색
# cv2.findContours( 이진화 이미지, 검색 방법, 근사화 방법 )
# return value => contours(윤곽선), hierachy(계층구조)
# contours : Numpy 구조의 배열로 검출된 윤곽선의 지점들
# hierachy : 윤곽선의 계층구조, 윤곽선의 속성정보

# 검색방법
# cv2.RETR_EXTERNAL : 외곽 윤곽선만 검출, 계층구조 구성 안함
# cv2.RETR_LIST     : 모든 윤곽선 검출, 계층구조 구성 안함
# cv2.RETR_CCOMP    : 모든 윤곽선 검출, 계층구조 2단계 구성
# cv2.RETR_TREE     : 모든 윤곽선 검출, 계층구조 모두 형성(TREE 구조)

# 근사화 방법
# cv2.CHAIN_APPROX_NONE      : 윤곽점들의 모든 점을 반환합니다.

# cv2.CHAIN_APPROX_SIMPLE    : 윤곽점들 단순화 수평, 수직 및 대각선 요소를 압축하고 끝점만 남겨 둡니다.

# cv2.CHAIN_APPROX_TC89_L1   : 프리먼 체인 코드에서의 윤곽선으로 적용합니다.

# cv2.CHAIN_APPROX_TC89_KCOS : 프리먼 체인 코드에서의 윤곽선으로 적용합니다.

contours, hierachy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


# 3. 
# cv2.drawContours()로 검출된 윤곽선 시각화
# cv2.drawContours(이미지, [윤곽선], 윤곽선 인덱스, (B,G,R), 두께, 선형타입)
# 윤곽선 인덱스 : 검출된 윤곽선 배열에서 몇번째 인덱스의 윤곽선을 그릴지를 의미
print("="*50)
print("len : " + str(len(contours)))
print("="*50)
max_iter = 0
max = 0
for i in range(len(contours)):
    if max < len(contours[i]):
        max = len(contours[i])
        max_iter = i
    # print( len(contours[i]) )
print(max_iter, max)

cv2.drawContours(src, [contours[max_iter]], 0, (0, 0, 255), 1)
cv2.imshow("src", src)

cv2.drawContours(white, [contours[max_iter]], 0, (0, 0, 255), 1)
cv2.imshow("white", white)

cv2.waitKey(0)
cv2.imwrite('./output/white.png', white)

# time.sleep(10)


cv2.destroyAllWindows()

# for i in range(len(contours)):
#     cv2.drawContours(src, [contours[i]], 0, (0, 0, 255), 1)
#     # cv2.putText(src, str(i), tuple(contours[i][0][0]), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)
#     cv2.putText(src, str(i), tuple(contours[i][0][0]), cv2.FONT_HERSHEY_COMPLEX, 0.2, (0, 255, 0), 1)
#     print(i, hierachy[0][i])
#     cv2.imshow("src", src)

#     print("="*50)
#     print(contours[i])
#     print("="*50)


#     cv2.waitKey(0)
#     # time.sleep(10)

# cv2.destroyAllWindows()
