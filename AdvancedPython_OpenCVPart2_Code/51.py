import cv2 as cv
import numpy as np
img1=cv.imread("3.jpg")
img2=cv.GaussianBlur(img1,(7,7),cv.BORDER_DEFAULT)
cv.imshow("temp",img2)
cv.waitKey(0)
