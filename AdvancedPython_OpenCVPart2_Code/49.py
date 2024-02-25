import cv2 as cv
import numpy as np
img1=cv.imread("3.jpg")
img2=cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
cv.imshow("temp",img2)
cv.waitKey(0)
