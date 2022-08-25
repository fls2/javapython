import cv2 
import numpy as np
img = cv2.imread('20220811/gora.jpg', cv2.IMREAD_COLOR)

cv2.imshow('img[:,:,0]',img[:,:,0])
cv2.waitKey(0)

img[:,:,2] = 0

cv2.imshow('gora',img)
cv2.waitKey(0)

test = img[:,:,1]>20 and img[:,:,2] >50
print(test)
