import cv2
img = cv2.imread("123.png",1)
#高斯去噪
img_gs = cv2.GaussianBlur(img,[5,5],0)
# 转灰度
img_gray = cv2.cvtColor(img_gs,cv2.COLOR_BGR2GRAY)
# 自适应二值化
_,binary_img = cv2.threshold(img_gray,0,255,cv2.THRESH_OTSU|cv2.THRESH_BINARY)
