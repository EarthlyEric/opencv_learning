import cv2
import numpy as np
video = cv2.VideoCapture(0)
  
ret, frame = video.read()
img = frame
cv2.rectangle(img,(50,50),(250,250),(0,0,255),5)  
cv2.imshow('Drawer', img)
cv2.waitKey(0)
cv2.destroyAllWindows()