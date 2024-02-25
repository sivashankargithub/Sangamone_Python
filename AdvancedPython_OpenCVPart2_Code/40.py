import cv2 as cv
import numpy as np
blank1=np.zeros((600,600,3),dtype='uint8')
blank1[100:480,100:480]=255,0,0
cv.imshow("temp",blank1)
cv.waitKey(0)
