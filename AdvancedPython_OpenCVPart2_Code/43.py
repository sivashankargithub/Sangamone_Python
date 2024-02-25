import cv2 as cv
import numpy as np
blank1=np.zeros((600,600,3),dtype='uint8')
cv.rectangle(blank1,(450,450),(10,10),(0,255,255),thickness=-1)
cv.imshow("temp",blank1)
cv.waitKey(0)
