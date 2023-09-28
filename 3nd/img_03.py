import cv2
import numpy as np

image = cv2.imread('3nd/01.jpg')
background = cv2.imread('3nd/02.jpg')


background = cv2.resize(background, (image.shape[1], image.shape[0]))

alpha = np.ones(image.shape, dtype=image.dtype) * 255  
image_with_alpha = cv2.merge((image, alpha))
background_with_alpha = cv2.merge((background, alpha))
alpha_blend = 0.5  
composite = cv2.addWeighted(image_with_alpha, alpha_blend, background_with_alpha, 1 - alpha_blend, 0)

cv2.imshow('Composite Image', composite)
cv2.waitKey(0)
cv2.destroyAllWindows()
