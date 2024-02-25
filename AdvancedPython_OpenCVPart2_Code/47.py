import cv2 as cv
import numpy as np
blank1=np.zeros((600,600,3),dtype='uint8')
cv.line(blank1,(0,300),(600,300),(0,0,255),thickness=2)
cv.line(blank1,(300,0),(300,600),(255,0,0),thickness=2)
cv.line(blank1,(0,0),(600,600),(0,255,0),thickness=2)
cv.line(blank1,(0,600),(600,0),(0,255,255),thickness=2)
cv.imshow("temp",blank1)
cv.waitKey(0)
