import cv2
import numpy as np

video = cv2.VideoCapture(0)

ret ,frame = video.read()

img = frame

contrast = 200
brightness = 50
output = img * (contrast/127 + 1) - contrast + brightness

output = np.uint8(output)

cv2.imshow('orignal', img)    
cv2.imshow('fixed', output) 
cv2.waitKey(0)                    
cv2.destroyAllWindows()