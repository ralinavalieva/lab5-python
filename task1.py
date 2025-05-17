import numpy as np
import matplotlib.pyplot as plt

# Генерация массива x
x = np.linspace(0, 10, 100)

# Вычисление y и z
y = np.sin(x)
z = np.cos(x)

# Построение графиков
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='sin(x)')
plt.plot(x, z, label='cos(x)')
plt.xlabel('x')
plt.ylabel('Значение функции')
plt.title('Графики sin(x) и cos(x)')
plt.legend()
plt.grid(True)
plt.show()
