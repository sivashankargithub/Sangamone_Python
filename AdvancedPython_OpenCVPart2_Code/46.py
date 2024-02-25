import cv2 as cv
import numpy as np
blank1=np.zeros((600,600,3),dtype='uint8')
shape1=blank1.shape
x1=int(shape1[0]*3/4)
y1=int(shape1[1]*3/4)
print(shape1)
radius=100
cv.circle(blank1,(x1,y1),radius,(250,250,25),thickness=-1)
cv.imshow("temp",blank1)
cv.waitKey(0)
