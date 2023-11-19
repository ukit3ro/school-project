import numpy as np
import matplotlib.pyplot as plt

def julia_fractal(x_lim, y_lim, c, N_max, n_points=800):
    x = np.linspace(-x_lim, x_lim, n_points)
    y = np.linspace(-y_lim, y_lim, n_points)

    A,B = np.meshgrid(x,y)

    Z = A + 1j*B 
    c = c
    img = np.zeros(Z.shape, dtype=float)

    for i in range(N_max):
        Z = Z**2 + c  # итерация Жюлиа
        mask = np.abs(Z) < 1000
        img += mask

    img = np.log(img + 1e-6)

    return img

def box_counting_dimension(image):
    n = image.shape[0]
    counts = []

    for k in range(1, n):
        stride = n // k
        count = 0
        for i in range(0, n, stride):
            for j in range(0, n, stride):
                if np.sum(image[i:i+stride, j:j+stride]) > 0:
                    count += 1
        counts.append(count)

    boxes = np.arange(1, n)
    counts = np.array(counts)

    log_boxes = np.log(boxes)
    log_counts = np.log(counts)

    coefficients = np.polyfit(log_boxes, log_counts, 1)
    dimension = coefficients[0]

    return dimension

# Параметры для фрактала Жюлиа
x_lim = 1.5
y_lim = 1.5
c = -0.75 + 0.11j
N_max = 800

# Создание фрактала Жюлиа
fractal_image = julia_fractal(x_lim, y_lim, c, N_max)

# Визуализация фрактала Жюлиа
plt.imshow(fractal_image, extent=(-x_lim, x_lim, -y_lim, y_lim), cmap="hot")
plt.colorbar()
plt.show()

# Вычисление коробочной размерности
dimension = box_counting_dimension(fractal_image)
print("Box-counting dimension:", dimension)