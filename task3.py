 import numpy as np

# Создание матрицы 5x5 со случайными целыми числами от 1 до 10
matrix = np.random.randint(1, 11, size=(5, 5))
print("Матрица:\n", matrix)

# Среднее значение элементов матрицы
mean_value = np.mean(matrix)
print("Среднее значение:", mean_value)

# Максимальный и минимальный элементы
max_value = np.max(matrix)
min_value = np.min(matrix)
print("Максимальный элемент:", max_value)
print("Минимальный элемент:", min_value)

# Сумма по столбцам
sum_columns = np.sum(matrix, axis=0)
print("Сумма по столбцам:", sum_columns)
