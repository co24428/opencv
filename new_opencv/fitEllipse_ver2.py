import cv2 
import glob
import os
import sys
from time import sleep

# dataPath = "/home/team/project/GAN/bean/data"
# normal_imgs = glob.glob(os.path.join(dataPath+"/normal_rotated_data",'*.jpg'))

# for img in normal_imgs:
#     imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
#     ret, thr = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY) 
#     _, contour, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
#     con = contour[1] 
#     (x, y), r = cv2.minEnclosingCircle(con) 
#     cv2.circle(img, (int(x), int(y)), int(r), (0, 0, 255), 2) 
#     ellipse = cv2.fitEllipse(con) 
#     cv2.ellipse(img, ellipse, (0, 255, 0), 2) 
#     cv2.imshow('img', img) 
#     cv2.waitKey(0) 
#     cv2.destroyAllWindows()

# dataPath = "/home/team/project/GAN/bean/data/broken_rotated_data/20200519_0_broken_take1_final_135.jpg"
# dataPath = "/home/team/project/GAN/bean/data/normal_rotated_data/20200520_0_normal_take1_final_134.jpg"

dataPath = "/home/team/project/GAN/bean/data"
# normal_imgs = glob.glob(os.path.join(dataPath+"/normal_rotated_data",'*.jpg'))
normal_imgs = glob.glob(os.path.join(dataPath+"/broken_rotated_data",'*.jpg'))
for x in normal_imgs:
    img = cv2.imread(x, cv2.IMREAD_COLOR)
    imgray = cv2.imread(x, cv2.IMREAD_GRAYSCALE)
    # imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    ret, thr = cv2.threshold(imgray, 50, 255, cv2.THRESH_BINARY) 
    cv2.imshow("img", img)
    cv2.imshow("imgray", imgray)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()

    _, contour, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
    print(len(contour))
    # sleep(10)
    con = contour[0] 
    (x, y), r = cv2.minEnclosingCircle(con) 
    # cv2.circle(img, (int(x), int(y)), int(r), (0, 0, 255), 2) 
    ellipse = cv2.fitEllipse(con) 
    cv2.ellipse(img, ellipse, (0, 255, 0), 1) 
    cv2.imshow("thr", thr)
    cv2.imshow('img', img) 
    cv2.waitKey(0) 
    cv2.destroyAllWindows()