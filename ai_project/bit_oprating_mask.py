import cv2
import numpy as np

photo = cv2.imread('img/77_leopard.jpg')
img = np.zeros(photo.shape[:2], dtype='uint8')

circle = cv2.circle(img.copy(), (200, 300), 120, 255, -1)
square = cv2.rectangle(img.copy(), (25, 25), (250, 350), 255, -1)

img = cv2.bitwise_and(photo, photo, mask=square)  # общее совпадение

# img = cv2.bitwise_and(circle, square)  # общее совпадение
# img = cv2.bitwise_or(circle, square)  # объединение полное
# img = cv2.bitwise_xor(circle, square)  # объединение реверс совпадение
# img = cv2.bitwise_not(circle)  # инверсия

cv2.imshow('Photo_Proba', img)
cv2.waitKey(2 * 1000)
