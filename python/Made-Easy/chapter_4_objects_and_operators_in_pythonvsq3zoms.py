# %%NBQA-CELL-SEPfaab7c
"Module on variables."


# %%NBQA-CELL-SEPfaab7c
import keyword


# %%NBQA-CELL-SEPfaab7c
print(keyword.kwlist)


# %%NBQA-CELL-SEPfaab7c
sample = 5
# переменная, которой присвоено значение 5
id(sample), type(sample)
# адрес в памяти или идентификатор объекта


# %%NBQA-CELL-SEPfaab7c
b"nilabh"


# %%NBQA-CELL-SEPfaab7c
ord("nilabh"[3]), ord("a"), chr(97)


# %%NBQA-CELL-SEPfaab7c
# Например:

print(chr(65))  # Output: 'A'
print(chr(97))  # Output: 'a'


# %%NBQA-CELL-SEPfaab7c
print(ord("A"))  # Output: 65
print(ord("a"))  # Output: 97


# %%NBQA-CELL-SEPfaab7c
# 1. Строки-комментарии:
# Это однострочный комментарий

"""
Это многострочный комментарий,
который может занимать
несколько строк.
"""
# 2. Документирующие строки (docstrings):


def my_function(var_a, var_b):
    """
    Возвращает сумму двух чисел a и b.

    Args:
        a (int): Первое число
        b (int): Второе число

    Returns:
        int: Сумма чисел a и b
    """
    return var_a + var_b


# %%NBQA-CELL-SEPfaab7c
variable_x = 2 + 3 * 4  # результат: 14
variable_x = (2 + 3) * 4  # результат: 20


# %%NBQA-CELL-SEPfaab7c
my_list = [1, 2, 3]
variable_y = my_list[0] + 2  # результат: 3


# %%NBQA-CELL-SEPfaab7c
my_dict = {"a": 1, "b": 2}
variable_z = my_dict["a"] + 2  # результат: 3
print(variable_z)


# %%NBQA-CELL-SEPfaab7c
variable_u = my_function(2, 3) * 4  # результат: 20
print(variable_u)


# %%NBQA-CELL-SEPfaab7c
my_string = "hello"
variable_p = len(my_string) + 2  # результат: 7
print(variable_p)


# %%NBQA-CELL-SEPfaab7c
# 1. Питер получает зарплату 12 000 в месяц. Напишите код для вычисления его сбе­
# режений к концу года, если он будет откладывать 20% своей зарплаты каждый
# месяц.

payment = 12000
savings = (payment * 12) * 0.2
print(savings)


# %%NBQA-CELL-SEPfaab7c
# 2. Расстояние между Мумбаи и Дели составляет 1422 км. Если Сундар едет на ма­
# шине со средней скоростью 72 км/ч, сколько времени ему потребуется, чтобы
# преодолеть это расстояние?
distance = 1422
average_speed = 72
time = distance / average_speed  # 19.75
minutes = time % 1 * 60  # 45"
print(int(time - time % 1), ":", int(minutes))


# %%NBQA-CELL-SEPfaab7c
# 3. Температура тела человека находится в диапазоне от 97 до 99° по Фаренгейту. Как этот диапазон будет выглядеть в градусах Цельсия?
celcium_lower = (97 - 32) * 5 / 9
celcium_upper = (99 - 32) * 5 / 9
print(round(celcium_lower, 1), round(celcium_upper, 1))


# %%NBQA-CELL-SEPfaab7c
# 4. Пусть дано шестизначное число.
# Напишите программу для вычисления суммы всех цифр этого числа.
num = 356789
num_str = str(num)
total_sum = 0
for i in num_str:
    total_sum += int(i)
print(total_sum)


# %%NBQA-CELL-SEPfaab7c
shop_a = 6500
shop_b = 8000
shop_c = 12000
shop_d = 4900
shop_e = 5600
lst_of_shops = [shop_a, shop_b, shop_c, shop_d, shop_e]
total_shops = sum(lst_of_shops)
for i in lst_of_shops:
    print(f"market_share_{i} = {int(round(i/total_shops,2)*100)}%")


# %%NBQA-CELL-SEPfaab7c
price = 1800
sell_price = price * 1.25
final_price = sell_price * 1.05
print(final_price)


# %%NBQA-CELL-SEPfaab7c
# 8. Найдите объем и площадь куба с диагональю 5 м.
diagonale = 5
edge = diagonale / (3) ** 0.5
volume = edge**3
square = 6 * edge**2
print(volume, square)


# %%NBQA-CELL-SEPfaab7c
edge_a = 3
edge_b = 4
edge_c = 5
square_a = edge_a**3
square_b = edge_b**3
square_c = edge_c**3
square_new_cube = square_a + square_b + square_c
edge_new_cube = square_new_cube**0.5
print(edge_new_cube)


# %%NBQA-CELL-SEPfaab7c
# 10. Дано шестизначное число. Напишите программу для
# получения числа с обрат­ным порядком цифр.

num = int(input("Введите шестизначное число: "))
reversed_num = str(num)[::-1]

# Вывести результат
print("Число с обратным порядком цифр:", reversed_num)
