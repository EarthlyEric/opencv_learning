import cv2

img1 = cv2.imread('3nd/01.jpg')
img2 = cv2.imread('3nd/02.jpg')
w = img1.shape[1]   
h = img1.shape[0]   

for i in range(w):
    img1[:,i,0] = img1[:,i,0]*((300-i)/300) + img2[:,i,0]*(i/300)  
    img1[:,i,1] = img1[:,i,1]*((300-i)/300) + img2[:,i,1]*(i/300)  
    img1[:,i,2] = img1[:,i,2]*((300-i)/300) + img2[:,i,2]*(i/300)  

show = img1.astype('float32')/255    
cv2.imshow('Result', show)

cv2.waitKey(0)       
cv2.destroyAllWindows()