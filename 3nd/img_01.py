import cv2
img = cv2.imread('./3nd/01.jpg')
logo = cv2.imread('./3nd/02.jpg')
output = cv2.addWeighted(img, 0.5, logo, 0.3, 50)


cv2.imshow('oxxostudio', output)
cv2.waitKey(0)      
cv2.destroyAllWindows()