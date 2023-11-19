""" import numpy as np
import matplotlib.pyplot as plt

def fractal_carpet(n):
    carpet = np.array([[1]])

    for _ in range(n):
        carpet = np.hstack((carpet, carpet, carpet))
        carpet = np.vstack((carpet, carpet, carpet))

        # Заменяем центральный квадрат на пустоту
        m = carpet.shape[0] // 3
        carpet[m:2 * m, m:2 * m] = 0

    return carpet

n = 5  # Количество итераций

carpet = fractal_carpet(n)

# Выводим фрактал на экран
plt.imshow(carpet, cmap='gray_r')
plt.axis('off')
plt.show()

# Вычисляем размерность фрактала методом Хаусдорфа
from scipy.spatial.distance import pdist, squareform

distances = pdist(np.argwhere(carpet == 1))
d = np.mean(squareform(distances))
dimension = -np.log(8) / np.log(d)
print(f"Размерность фрактала (метод Хаусдорфа): {dimension}")

# Оцениваем степень самоподобия фрактала методом Бокса
def box_method(data):
    n = len(data)
    lengths = []
    
    for i in range(1, n + 1):
        distances = np.abs(data[:n - i] - data[i:])
        lengths.append(np.mean(distances))
        
    return lengths

self_similarity = box_method(np.argwhere(carpet == 1))
print(f"Степень самоподобия фрактала (метод Бокса): {self_similarity}") """

import numpy as np
import matplotlib.pyplot as plt

# Задание параметров
width, height = 800, 800
xmin, xmax, ymin, ymax = -1.0, 1.0, -1.5, 1.5
max_iter = 256

def new_fractal(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z*z + c  # ввожу новую функцию для создания нового вида фрактала
    return max_iter

def draw_fractal(width, height, xmin, xmax, ymin, ymax, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            n3[i][j] = new_fractal(r1[i] + 1j*r2[j], max_iter)
    plt.imshow(n3, extent=(xmin, xmax, ymin, ymax))
    plt.show()

draw_fractal(width, height, xmin, xmax, ymin, ymax, max_iter)
