import cv2

video = cv2.VideoCapture(0)
  
ret, frame = video.read()
img = frame
size = img.shape        
level = 15               
h = int(size[0]/level)  
w = int(size[1]/level)   
mosaic = cv2.resize(img, (w,h), interpolation=cv2.INTER_LINEAR)   
mosaic = cv2.resize(mosaic, (size[1],size[0]), interpolation=cv2.INTER_NEAREST)
cv2.imshow('馬賽克', mosaic)
cv2.waitKey(0)          
cv2.destroyAllWindows()