import numpy as np
import matplotlib.pyplot as plt

# Генерация двух массивов случайных чисел
x_data = np.random.rand(5)
y_data = np.random.rand(5)

# Построение диаграммы рассеяния
plt.scatter(x_data, y_data, c='blue', alpha=0.5)
plt.title('Диаграмма рассеяния для случайных данных')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

