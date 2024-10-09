# %%NBQA-CELL-SEPfaab7c
"Module om intospection."


# %%NBQA-CELL-SEPfaab7c
import matplotlib.pyplot as plt
import numpy as np


# %%NBQA-CELL-SEPfaab7c
lst = [4, 45, 42]
hash(0xFE9E1DDD)


# %%NBQA-CELL-SEPfaab7c
hash(0x22F5922D)


# %%NBQA-CELL-SEPfaab7c
# Бинарные операторы

variable_a = True
variable_b = False


# %%NBQA-CELL-SEPfaab7c
variable_a & variable_b  # True if a and b  True бинарный оператор "И"
variable_a | variable_b  # True if a or b True
(
    variable_a ^ variable_b
)  # "Исключающее или". Либо a либо b - True но не обе одновременно. Исп-ся для bool


# %%NBQA-CELL-SEPfaab7c
lst2 = ["hjh", 1, []]
lst2[2] = {5}
print(lst2)


# %%NBQA-CELL-SEPfaab7c
arr = np.array([1, 1000, 121]).astype("int8")

print(arr)


# %%NBQA-CELL-SEPfaab7c
variable_n = "math"
# variable_n[0] = "b" # вываливается ошибка, те str - неизмен тип данных
print(variable_n)


# %%NBQA-CELL-SEPfaab7c
print(list(variable_n))


# %%NBQA-CELL-SEPfaab7c
variable_h = np.array([[4, 5], [3, 8]]).astype("int32")
print(variable_h)


# %%NBQA-CELL-SEPfaab7c
# Отображаем радиус-вектор на графике
vector_v = np.array([2, -1])  # указываем координату конца вектора (tail) [2,-1]
plt.plot(
    [0, vector_v[0]], [0, vector_v[1]]
)  # отображаем на гарфике: (axis=1:[head, tail], axis=0:[head, tail])
plt.axis([-3, 3, -3, 3])  # Задаем размер осей: OX(axis=1) (-3, 3), OX(axis=0):(-3, 3)
