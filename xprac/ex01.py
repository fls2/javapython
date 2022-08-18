import cv2
import numpy as np
img = cv2.imread('wine.jpg',cv2.IMREAD_COLOR)


cv2.imshow('wine',img)
cv2.waitKey(0)

img[:,:,2] = 0

