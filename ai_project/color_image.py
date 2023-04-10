import cv2
import numpy as np

img = cv2.imread('img/77_leopard.jpg')

# img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

cv2.imshow('Photo_Proba', img)
cv2.waitKey(2 * 1000)
