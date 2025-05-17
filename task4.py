import numpy as np
import matplotlib.pyplot as plt

# Используем ту же матрицу из задания 3
matrix = np.random.randint(1, 11, size=(5, 5))

plt.figure(figsize=(6, 5))
im = plt.imshow(matrix, cmap='viridis')

# Добавление цветовой шкалы
plt.colorbar(im)

# Аннотация чисел в ячейках
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        plt.text(j, i, str(matrix[i, j]), ha='center', va='center', color='white')

plt.title('Тепловая карта матрицы')
plt.xlabel('Столбцы')
plt.ylabel('Строки')
plt.show()
