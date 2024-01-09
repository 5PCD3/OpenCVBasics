# Crop

import os
import cv2


img = cv2.imread(os.path.join('.','data','bird.jpg'))
cropped_img = img[20:420,220:600]
print(img.shape)
print(cropped_img.shape)


cv2.imshow('img', img)
cv2.imshow('croped_img', cropped_img)
cv2.waitKey(0)