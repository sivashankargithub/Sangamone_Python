import cv2 as cv
import numpy as np
blank1=np.zeros((600,600,3),dtype='uint8')
cv.circle(blank1,(300,300),200,(250,250,25),thickness=-1)
cv.imshow("temp",blank1)
cv.waitKey(0)
