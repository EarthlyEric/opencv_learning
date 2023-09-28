import cv2
import numpy as np

mask = np.zeros((300, 300, 3), dtype='uint8')
cv2.circle(mask, (150, 150), 100, (255, 255, 255), -1)
mask = cv2.GaussianBlur(mask, (35, 35), 0)
mask = mask / 255

img = cv2.imread('./3nd/02.jpg')
img = cv2.resize(img, (300, 300))
img = img / 255

bg = np.zeros((300, 300, 3), dtype='uint8')
bg = 255 - bg
bg = bg / 255

out = bg * (1 - mask) + img * mask
out = (out * 255).astype('uint8')

cv2.imshow('ds', out)
cv2.waitKey(0)
cv2.destroyAllWindows()
