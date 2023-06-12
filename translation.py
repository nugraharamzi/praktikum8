import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("ramzi.jpg") 
h,w = image.shape[:2]
half_height, half_width = h//4, w//8
transition_matrix = np.float32([[1, 0, half_width],[0, 1,half_height]])
img_transition = cv2.warpAffine(image,transition_matrix, (w, h))
plt.imshow(cv2.cvtColor(img_transition,cv2.COLOR_BGR2RGB))
plt.title("Translation") 
plt.show()