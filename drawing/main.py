import os
import cv2
import numpy as np


img=cv2.imread(os.path.join('.','data','white_.jpg'))
print(img.shape)


# Line
cv2.line(img , (150,200),(400,550),(0,255,0),3)

# Rectangle
cv2.rectangle(img,(150,200),(100,400),(0,0,255),5)

# Circle
cv2.circle(img,(225,200),66,(0,225,0),-10)

# Text
cv2.putText(img , 'hey you!',(235,350),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)