import cv2
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("3nd/haarcascade_frontalface_default.xml")
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.resize(frame,(540,320))              
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   
    faces = face_cascade.detectMultiScale(gray)      
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)   
    cv2.imshow('oxxostudio', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()