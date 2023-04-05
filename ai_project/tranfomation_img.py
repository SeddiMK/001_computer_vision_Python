import cv2
import numpy as np


img = cv2.imread('img/77_leopard.jpg')
new_img = np.zeros(img.shape, dtype='uint8')

# //-делим получилось целое число
img = cv2.resize(img, (img.shape[1] // 4, img.shape[0] // 3))
# img = cv2.flip(img, -1) # -1- img отзеркалена по гориз, вертикали и т.д.

# def rotate(img_param, angle): # функиця вращения img
#     height, width = img_param.shape[:2]
#     point = (width // 2, height // 2)
#     matr = cv2.getRotationMatrix2D(point, angle, 1) # 1-при вращении изображение НЕ увеличивается, если надо увеличение в 2 раза, то ставить 2
#     return cv2.warpAffine(img_param, matr, (width, height))

# img = rotate(img, 90)
# ============================================================================

# def transform(img_param, x, y): # смещение картинки
#     matr = np.float32([[1, 0, x], [0, 1, y]])
#     return cv2.warpAffine(img_param, matr, (img_param.shape[1], img_param.shape[0]))
# img = transform(img, 30, 200)
# ============================================================================
 # находим контуры изображения
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5, 5), 0)
img = cv2.Canny(img, 100, 140)
con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# print(con)

# ============================================================================
cv2.drawContours(new_img, con, -1, (230, 32, 43), 1) # рисуем картунку
# ============================================================================

cv2.imshow('Leop', new_img)  # Просмотр картинки
cv2.waitKey(2 * 1000)
