import cv2

# fname = './image/broken.png'
fname = './image/insect_damage_resize.jpg'
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
src = cv2.imread(fname , cv2.IMREAD_COLOR)
gray = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)

ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
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

contours, hierachy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

# 

for i in range(len(contours)):
    cv2.drawContours(src, [contours[i]], 0, (0, 0, 255), 2)
    cv2.putText(src, str(i), tuple(contours[i][0][0]), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
    print(i, hierachy[0][i])
    cv2.imshow("src", src)
    cv2.waitKey(0)

cv2.destroyAllWindows()