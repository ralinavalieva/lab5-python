 import numpy as np
import matplotlib.pyplot as plt

# Генерация 1000 случайных чисел
data = np.random.normal(loc=0, scale=1, size=1000)

# Построение гистограммы
plt.figure(figsize=(8, 5))
plt.hist(data, bins=20, edgecolor='black')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.title('Гистограмма случайных данных (нормальное распределение)')
plt.grid(True)
plt.show()
