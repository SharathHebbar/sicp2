import cv2
import numpy as np

input_image = cv2.imread('/home/pi/Desktop/image.jpg')
filtered = cv2.adaptiveThreshold(input_image.astype(np.uint8), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 41, 3)
kernel = np.ones((5,5), np.uint8)
opening = cv2.morphologyEx(filtered, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
