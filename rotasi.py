import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("ramzi.jpg")
h, w = image.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((w/2,h/2), -180, 0.5)
rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))
plt.imshow(cv2.cvtColor(rotated_image,cv2.COLOR_BGR2RGB))
plt.title("Rotation") 
plt.show()