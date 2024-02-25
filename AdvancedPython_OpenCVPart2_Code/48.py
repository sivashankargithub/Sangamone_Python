import cv2 as cv
import numpy as np
img1=cv.imread("3.jpg")
img2=cv.flip(img1,0)
img3=cv.flip(img1,1)
img4=cv.flip(img1,-1)
cv.imwrite("banana1.jpg",img1)
cv.imwrite("banana2.jpg",img2)
cv.imwrite("banana3.jpg",img3)
cv.imwrite("banana4.jpg",img4)
cv.imshow("temp",img4)
cv.waitKey(0)
