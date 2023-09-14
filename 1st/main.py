import cv2
  
video = cv2.VideoCapture(0)
  

ret, frame = video.read()

cv2.imwrite("cv2_base.png",frame)

flip_1  = cv2.flip(frame,0)
flip_2 = cv2.flip(frame,1)
flip_3 = cv2.flip(frame,-1)
cv2.imshow("flip_1",flip_1)
cv2.imshow("flip_2",flip_2)
cv2.imshow("flip_3",flip_2)
cv2.imwrite("flip_1.png",flip_1)
cv2.imwrite("flip_2.png",flip_2)
cv2.imwrite("flip_3.png",flip_3)
   
cv2.waitKey(0)   
video.release()

cv2.destroyAllWindows()