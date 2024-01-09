import os

import cv2

# Read Webcam

Webcam = cv2.VideoCapture(0)

# Visualize Webcam

while True :
    ret , frame = Webcam.read()

    
    cv2.imshow('frame',frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

Webcam.release()
cv2.destroyAllWindows()