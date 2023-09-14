import cv2
video = cv2.VideoCapture(0)
  

ret, frame = video.read()

cv2.imwrite("cv2_base.png",frame)
img_gary = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
img_gary = cv2.medianBlur(img_gary, 7)                 
output = cv2.Laplacian(img_gary, -1, 1, 5)        
cv2.imshow('灰階', output)

cv2.waitKey(0)                               
cv2.destroyAllWindows()