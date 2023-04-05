import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# cap.set(3, 500)  # 3-ширина картинки
# cap.set(4, 300)  # 4-высота картинки
while True:
    success, img = cap.read()
    cv2.imshow('Result Camera', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# //-делим получилось целое число
img = cv2.resize(img, (img.shape[1] // 3, img.shape[0] // 2))
# размытие изображения # (9, 9) -задавать только не четные значения
img = cv2.GaussianBlur(img, (9, 9), 0)
# перевод изображения в черно белый цвет
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# параметры углов картинки # приведение картинки в бинарцый формат 1 и 0 # 90, 90 -пороги(точность обводок белым цветом). 30,30 - больше точность
img = cv2.Canny(img, 200, 200)

# np.uint8 - только целые положительные числа
kernel = np.ones((5, 5), np.uint8)
# уменьшили углы, увеличили жирность, увеличили обводку
img = cv2.dilate(img, kernel, iterations=1)


img = cv2.erode(img, kernel, iterations=1)  # уменьшили количество белых точек


# Просмотр картинки #  img[0:200, 0:300] -Обрезка картинки
cv2.imshow('Leop', img)
# print(img.shape)  # 3-количество слоев
cv2.waitKey(2 * 1000)  # 0-показывать бесконечно
