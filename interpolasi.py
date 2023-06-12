import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread("ramzi.jpg")
fig, ax = plt.subplots(1, 3, figsize=(16, 8))
# image size being 0.15 times of it's original size
image_scaled = cv2.resize(image, None, fx=0.15, fy=0.15)
ax[0].imshow(cv2.cvtColor(image_scaled, cv2.COLOR_BGR2RGB))
ax[0].set_title("Linear Interpolation Scale")
# image size being 2 times of it's original size
image_scaled_2 = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
ax[1].imshow(cv2.cvtColor(image_scaled_2, cv2.COLOR_BGR2RGB))
ax[1].set_title("Cubic Interpolation Scale")
# image size being 0.15 times of it's original size
image_scaled_3 = cv2.resize(image, (200, 400), interpolation=cv2.INTER_AREA)
ax[2].imshow(cv2.cvtColor(image_scaled_3, cv2.COLOR_BGR2RGB))
ax[2].set_title("Skewed Interpolation Scale") 
plt.show()