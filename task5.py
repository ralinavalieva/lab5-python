 import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)#100 точ от 0 до 10, равномерно распр.

fig, axs = plt.subplots(1, 3, figsize=(15, 4))

# Область 1: линейный график y=x^2
axs[0].plot(x, x**2)
axs[0].set_title('y = x^2')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')

# Область 2: точечный график случайных точек
np.random.seed(0) # для воспроизводимости
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)
axs[1].scatter(x_scatter, y_scatter)
axs[1].set_title('Случайные точки')
axs[1].set_xlabel('X')
axs[1].set_ylabel('Y')

# Область 3: столбчатая диаграмма для категориальных данных
categories = ['A', 'B', 'C']
values = [3, 7, 2]
axs[2].bar(categories, values)
axs[2].set_title('Категориальные данные')

plt.tight_layout()
plt.show()
