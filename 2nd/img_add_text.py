import cv2


video = cv2.VideoCapture(0)
  
ret, frame = video.read()
img = frame
text = 'Hello World !'
org = (20,90)
fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 2.5
color = (0,0,255)
thickness = 5
lineType = cv2.LINE_AA
cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType)
cv2.imshow('Text', img)
cv2.waitKey(0)
cv2.destroyAllWindows()