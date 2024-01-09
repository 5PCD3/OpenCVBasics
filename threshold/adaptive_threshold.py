import os
import cv2

img=cv2.imread(os.path.join('.','data','handwritting.jpg'))
img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh=cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,30)

#ret,thresh=cv2.threshold(img_gray,80,255, cv2.THRESH_BINARY)

cv2.imshow('img',img)
cv2.imshow('thresh',thresh)


cv2.waitKey(0)