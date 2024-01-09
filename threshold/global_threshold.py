import os
import cv2

img=cv2.imread(os.path.join('.','data','bird.jpg'))
img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


ret,thresh=cv2.threshold(img_gray,80,255, cv2.THRESH_BINARY)
blurred_img=cv2.blur(thresh,(9,9))
ret,thresh_2=cv2.threshold(blurred_img,80,255, cv2.THRESH_BINARY)



cv2.imshow('img_gray',img_gray)
cv2.imshow('img',img)
cv2.imshow('thresh',thresh)
cv2.imshow('thresh_2',thresh_2)
cv2.waitKey(0)