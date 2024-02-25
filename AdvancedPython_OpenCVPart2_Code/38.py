import cv2 as cv
img1=cv.imread("2.jpg")
img2=cv.resize(img1,(400,400))
cv.imshow("temp",img2)
cv.waitKey(0)
