import os
import cv2

img=cv2.imread(os.path.join('.','data','batman.jpeg'))


k_size = 7
blurred_img=cv2.blur(img,(k_size,k_size))
G_blurred_img=cv2.GaussianBlur(img,(k_size,k_size),3)
M_blurred_img=cv2.medianBlur(img,k_size)


cv2.imshow('img',img)
cv2.imshow('blurred_img',blurred_img)
cv2.imshow('G_blurred_img',G_blurred_img)
cv2.imshow('M_blurred_img',M_blurred_img)
cv2.waitKey(0)
