import time
import cv2

img = cv2.imread('wine.jpg',cv2.IMREAD_COLOR)

start_time = time.time()
for i in range(10):
    img[i] = [255,255,255]

cv2.imshow('wine',img)
cv2.waitKey(0)

start_time = time.time()
img[230:,130:] = [0,0,0]

cv2.imshow('wine',img)
cv2.waitKey(0)
