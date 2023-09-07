import cv2
  
video = cv2.VideoCapture(0)
  
while(True):
    ret, frame = video.read()

    if cv2.waitKey(1)& 0xFF == ord('1'):
        img = frame
        cv2.flip(img,1)
        cv2.imwrite("cv2_flip_horizen.png",img=img)
        cv2.imshow("cv2_output",img)
    
    if cv2.waitKey(1)& 0xFF == ord('2'):
        img = frame
        cv2.flip(img,-1)
        cv2.imwrite("cv2_flip_updown.png",img=img)
        cv2.imshow("cv2_output",img)
    
    if cv2.waitKey(1)& 0xFF == ord('3'):
        img = frame
        cv2.flip(img,-1)
        cv2.imwrite("cv2_flip_updown.png",img=img)
        cv2.imshow("cv2_output",img)
    
    if cv2.waitKey(1)& 0xFF == ord('4') :
        img = frame
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY); 
        cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        cv2.imwrite("cv2_blackwhite.png",img=img)
        cv2.imshow("cv2_blackwhite",img)

    if cv2.waitKey(1)& 0xFF == ord('w') :
        break
    
video.release()

cv2.destroyAllWindows()