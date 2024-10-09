# %%NBQA-CELL-SEPfaab7c
"""Модуль посвящен теории множеств."""


# %%NBQA-CELL-SEPfaab7c
fruits = {"banana", "apple", "orange"}


# %%NBQA-CELL-SEPfaab7c
wrong_empty_set: dict[float, str] = {}
print(type(wrong_empty_set))


# %%NBQA-CELL-SEPfaab7c
correct_empty_set: set[str] = set()
print(type(correct_empty_set))


# %%NBQA-CELL-SEPfaab7c
color_list: list[str] = ["red", "green", "blue", "purple", "purple"]
color_set = set(color_list)
print(color_set)


# %%NBQA-CELL-SEPfaab7c
numbers: list[int] = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
# Единственное отличие со списковыми включениями - это
# использование фигурных скобок виесто квадратных
even_numbers = {number for number in numbers if number % 2 == 0}
print(even_numbers)


# %%NBQA-CELL-SEPfaab7c
# Множество кортежей (tuple)
records: set[tuple[str, int]] = {
    ("Москва", 17_200_000),
    ("Санкт - Петербург", 5_400_000),
    ("Новосибирск", 1_600_000),
    ("Москва", 17_200_000),
}
for city, population in records:
    print(city)


# %%NBQA-CELL-SEPfaab7c
tremendously_huge_set: set[str] = {"red", "green", "blue"}
if "green" in tremendously_huge_set:
    print("Green is there!")
else:
    print("Unfortunately, there is no green...")

if "purple" in tremendously_huge_set:
    print("Purple is there!")
else:
    print("Unfortunately, there is no purple...")


# %%NBQA-CELL-SEPfaab7c
even_numbers = {i for i in range(100) if i % 2 == 0}
# Мощность мжножества
cardinality = len(even_numbers)
print(cardinality)


# %%NBQA-CELL-SEPfaab7c
colors: set[str] = {"red", "green", "blue"}
# Элементы множества можно перебрать с помощью цикла for
for color in colors:
    print(color)
# Множества можно использовать там, где ожидается iterable - объект
color_counter = dict.fromkeys(colors, 1)
print(color_counter)


# %%NBQA-CELL-SEPfaab7c
my_fruits = {
    "banana",
    "apple",
    "orange",
}
your_fruits = {"apple", "banana", "orange"}
print(my_fruits == your_fruits)


# %%NBQA-CELL-SEPfaab7c
even_numbers = {i for i in range(10) if i % 2 == 0}
odd_numbers = {i for i in range(10) if i % 2 == 1}
#  Очевидно, что множества чётных и нечётных чисел не пересекаются
if even_numbers.isdisjoint(odd_numbers):
    print("Множества не пересекаются!")


# %%NBQA-CELL-SEPfaab7c
# Множество чисел Фибоначчи меньших 100
fibonacci_numbers: set[int] = {0, 1, 2, 3, 34, 5, 8, 13, 21, 55, 89}
# Множество натуральных чисел меньших 100
natural_numbers = set(range(100))
# Множество чисел Фибоначчи является подмножеством множества
# натуральных чисел
if fibonacci_numbers.issubset(natural_numbers):
    print("Подмножетсво")
# В свою очередь множетсво натуральных чисел является
# надмножетсвом множетсва чисел Фибоначи
if natural_numbers.issuperset(fibonacci_numbers):
    print("Надмножество")
