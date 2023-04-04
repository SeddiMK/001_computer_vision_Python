import cv2
import numpy as np

photo = np.zeros((450, 450, 3), dtype='uint8')  # 3-у картинки 3 слоя

# RGB - стандарт
# BRG - формат OpenCV
# photo[:] = 119, 201, 195  # [:] - меняем цвет ширине и высоте
# photo[10:150, 200:280] = 119, 201, 195  #

# (30, 80) - координата начала; (60, 100) - размеры; thickness=3 - жирность линии; thickness=cv2.FILLED - полностью зальет всю фигуру
# cv2.rectangle(photo, (30, 80), (60, 100), (100, 210, 195), thickness=3)


cv2.line(photo, (0, 20), (100, 0), (100, 210, 195), thickness=3)

cv2.imshow('Photo_Proba', photo)
cv2.waitKey(2 * 1000)
ы
