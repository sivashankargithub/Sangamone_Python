import cv2 as cv
import numpy as np
img1=cv.imread("3.jpg")
img2=cv.Canny(img1,50,50)
cv.imshow("temp",img2)
cv.waitKey(0)
