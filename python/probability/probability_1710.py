"""Module 1.

Types of events, scipy, numpy.
"""

# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: base
#     language: python
#     name: python3
# ---

# + id="sV0gfOzBLMPy"
from typing import Callable

import numpy as np
import scipy as sc
from scipy import optimize
from scipy.optimize import OptimizeResult

# # Виды событий


def certain_event() -> int:
    """This function returns 1 as 100%.

    Returns:
        int: 1
    """
    return 1


# set?


def impossible_event() -> int:
    """This function returns 0 as impossible event.

    Returns:
       int: 0
    """
    return 0


# +
def random_event(successful_outcomes: float, total_outcome: float) -> float:
    """This function returns 0 as impossible event.

    Parameters:

    successful_outcomes: float
    total_outcome: float

    Returns:
       float: division of successful_outcomes on total_outcomes
    """
    return successful_outcomes / total_outcome


# Вызов функции с правильными аргументами
result = random_event(50, 1000)
print(result)


# def __init__(self, iterable: Iterable[_T], /)
# -> None: ... -  до / -  позиционные аргументы,
# а после / - ключевые
# Iterable[_T] -параметр является итерируемым объектом,
#     и содержит элементы типа _T
# _T — это обобщённый тип (generic),
# который представляет собой любой тип данных


def incompatible_events() -> None:
    """Calculate and print the probabilities of two incompatible events.

    The function initializes two events and calculates their probabilities
    based on the total number of outcomes.

    Args:
        None
    """
    event_a = {1, 2}
    event_b = {3, 4}
    total_outcomes = 6
    p_a = len(event_a) / total_outcomes
    p_b = len(event_b) / total_outcomes
    print(p_a, p_b)


incompatible_events()

# Противоположные события


def complementary_events() -> float:
    """Calculate the probability of the complement of an event.

    This function calculates the probability of event A and its complement.

    Returns:
        float: The probability of the complement of event A, rounded to two decimal places.
    """
    total_outcomes = 6
    event_a = {6}
    p_a = len(event_a) / total_outcomes
    p_not_a = 1 - p_a
    return round(p_not_a, 2)


complementary_events()

# Полная группа событий


def complete_group() -> float:
    """Calculate the probability of a complete group of events.

    This function calculates the probability of all possible outcomes.

    Returns:
        float: The probability of the complete group.
    """
    event = {1, 2, 3, 4, 5, 6}
    total_outcomes = 6
    p_a = len(event) / total_outcomes
    return p_a


complete_group()

# # Знакомство с библиотеками scipy, numpy

# Pi, e, infinity, -inf, +inf, none, none, none
print(np.pi, np.e, np.inf, -np.inf, np.inf, np.nan, np.nan, np.nan)

# корень , корень кубический, квадрат
print(np.sqrt(4), np.cbrt(9), np.square(4))

# x - complex number
print(np.abs(2 - 4), np.absolute(8 - 7))  # модуль числа
print(np.fabs(4.002 - 5.07))  # только действительные числа

# функция знака
# преобразование любых значений массива в 0,1,-1
# x > 0 1; x < 0 -1, x = 0 0
print(np.sign(-12), np.sign(0), np.sign(2))


# показательная функция
print(np.exp(2))
# возведение в степень
print(np.power(2, 4))
# 2 в степень 4
print(np.exp2(4))


# Натуральный логарифм — это логарифм, где в качестве основания используется число e (примерно равное 2,71828). Для вычисления натурального логарифма  используется функция numpy.log().

# ln -  e≈2.718 натуральный логарифм
# lg - 10 - логарифм 10 степени
print(np.log10(100))
# log по основанию 2
print(np.log2(8))

# [тригонометрические функции](https://numpy.org/doc/2.0/reference/generated/numpy.tan.html)
# -

# функция np.arcsin принимает значения только в диапазоне от -1 до 1. Когда вы передаете ей 5, это приводит к ошибке "invalid value encountered in arcsin", потому что 5 выходит за этот диапазон.

# + colab={"base_uri": "https://localhost:8080/"} id="79CKCLB6LMQu" outputId="80cb817e-e7b0-4cea-9b27-2e306a171982"
# тригонометрические функции
print(np.sin(5), np.cos(1), np.tan(5), np.arcsin(1), np.arctan(0.5))


print(np.around(4.5845454, 2))  # or np.round(4.5845454, 2)
print(np.arange(1, 5))

# Пример массива с дробными числами
values = np.array([1.5, -2.3, 3.7, -4.9, 5.0])

# Преобразование значений в целые числа (тип int)
int_values = np.ndarray.astype(
    values,
    dtype=np.int8,
)  # Приведение к целому типу (устаревшая функция, лучше использовать np.astype(int))

# Округление значений к бaлижайшему целому числу (вниз к нулю)
fixed_values = np.fix(
    values,
)  # Возвращает ближайшее целое число, не превышающее значение по модулю

# Округление вниз (к меньшему целому числу)
floor_values = np.floor(values)  # Округляет до ближайшего меньшего целого числа

# Округление вверх (к большему целому числу)
ceil_values = np.ceil(values)  # Округляет до ближайшего большего целого числа

# Уточнение на случай, если вы хотите вызвать ceil как функцию
# ceil_function = np.ceil  # Сохраняет ссылку на функцию ceil

# Отбрасывание дробной части (округление до нуля)
trunc_values = np.trunc(values)  # Удаляет дробную часть числа, оставляя только целую

# Вывод результатов
print("Исходные значения:", values)
print("Преобразованные в int:", int_values)
print("Округление к нулю:", fixed_values)
print("Округление вниз:", floor_values)
print("Округление вверх:", ceil_values)
print("Отбрасывание дробной части:", trunc_values)

# + [markdown] id="xwwR9GuTAVHt"
# # scipy


# 19
# Факториал числа
# Факториал числа n (n!) - произведение всех положительных целых чисел от 1 до n.
factorial_result = sc.factorial(5)  # 5! = 5 * 4 * 3 * 2 * 1 = 120
print("Факториал 5:", factorial_result)

# Комбинации
# Функция sc.comb(n, k) возвращает количество способов выбрать
# k элементов из n без учета порядка.
# Функция sc.binom(n, k) также возвращает количество комбинаций и является синонимом sc.comb(n, k).
comb_result = sc.comb(10, 1)  # C(10, 1) = 10
print("Комбинации из 10 по 1:", comb_result)

# Пример с массивами
# Здесь мы выбираем различные количества элементов (1, 2 и 3) из одного и того же n = 10.
comb_array_result = sc.comb([10], [1, 2, 3])  # Возвращает массив [10, 45, 120]
print("Комбинации из 10 по [1, 2, 3]:", comb_array_result)

# Перестановки
# Функция sc.perm(n, k) возвращает количество способов расположить k элементов из n.
perm_result = sc.perm(5, 4)  # P(5, 4) = 5! / (5-4)! = 5 * 4 * 3 * 2 = 120
print("Перестановки из 5 по 4:", perm_result)

# Пример с массивами
# Здесь мы выбираем перестановки для двух наборов: [5, 6, 7] и [4, 3, 2].
perm_array_result = sc.perm([5, 6, 7], [4, 3, 2])
# Возвращает массив с количеством перестановок для каждого соответствующего случая.
print("Перестановки для [5,6,7] и [4,3,2]:", perm_array_result)

# + [markdown] id="DGKNMC_kBcUS"
# ▎Объяснения функций:
#
# • sc.factorial(n): Вычисляет факториал числа n. Например, sc.factorial(5) возвращает 120, поскольку 5! = 120.
#
# • sc.comb(n, k): Вычисляет количество сочетаний (комбинаций) из n по k, то есть количество способов выбрать k элементов из n без учета порядка. Например, sc.comb(10, 1) возвращает 10, так как можно выбрать один элемент из десяти.
#
# • sc.binom(n, k): Это синоним функции sc.comb(n, k), которая также вычисляет количество сочетаний.
#
# • sc.perm(n, k): Вычисляет количество перестановок из n по k, то есть количество способов расположить k элементов из n. Например, sc.perm(5, 4) возвращает 120, так как это количество способов разместить четыре элемента из пяти.
#
# Эти функции полезны для комбинаторных расчетов в различных областях математики и статистики

# + colab={"base_uri": "https://localhost:8080/"} id="gXmzEGNwCBeh" outputId="80970d56-5085-468c-f216-21444752f44e"
# 20
# Функция гамма
# sc.gamma(x) вычисляет значение функции гамма для заданного x.
# Функция гамма является обобщением факториала для вещественных и комплексных чисел.
gamma_result = sc.gamma(5)  # gamma(5) = 4! = 24
print("Гамма 5:", gamma_result)

# Оптимизация функции
# sc.optimize.minimize() используется для нахождения минимума заданной функции.
# Она принимает несколько аргументов, включая функцию, начальное значение и метод оптимизации.

# +
# Функция гамма
# Определяем функцию, которую мы хотим минимизировать.
# В данном случае мы минимизируем функцию y = -f(x), где f(x) = x^3 - 3x^2 + x + 1
gamma_result_1: float = sc.gamma(5)  # gamma(5) = 4! = 24
print("Гамма 5:", gamma_result_1)

# Оптимизация функции
# Определяем функцию, которую мы хотим минимизировать.
fun: Callable[[float], float] = lambda x_: -(x_**3 - 3 * x_**2 + x_ + 1)

# Начальное значение для поиска минимума (в данном случае x = 0)
initial_guess: int = 0

# Используем метод minimize для нахождения минимума функции fun
res: OptimizeResult = optimize.minimize(fun, initial_guess)

# res.x содержит значение x, при котором функция достигает минимума
print("Минимум функции достигается при x =", res.x)

# + [markdown] id="uPM0x3zNK4r6"
# метод Монте-Карло
#
# Метод статистических испытаний - генерация случайный чисел с требуемым законом распределения, моделирование данных

# + id="rTX6MFVKK4sg" outputId="255c0e00-7e81-4b2f-e013-85453d0d8a53"
# моделирование эксперимента, данных - Монте-Карло
print(np.random.binomial(1, 0.5, size=10).mean())


# # Задачи


#     Сложение вероятностей используется, когда мы хотим узнать вероятность того, что произойдет одно из двух несовместных событий (например, выпадет либо 1, либо 2 на кубике).
#     Умножение вероятностей используется для вычисления вероятности одновременного наступления двух независимых событий.

# + [markdown] id="kZWLBuqlMlGT"
# ## 1

# + [markdown] id="sCak9ImVK4si"
# Предположим, у нас есть мешок с 5 синими шарами, 3 зелеными шарами и 2 красными шарами. Мы случайным образом вытаскиваем один шар из мешка. Какова вероятность того, что выбранный шар будет синим?

# + colab={"base_uri": "https://localhost:8080/"} id="MV1kC1siMERl" outputId="08f48560-fb60-4d77-cfb7-a0a5588a779b"
# Определяем количество шаров
blue_balls: int = 5
green_balls: int = 3
red_balls: int = 2

# Общее количество шаров
total_balls: int = blue_balls + green_balls + red_balls

# Вероятность выбрать синий шар
probability_blue: float = blue_balls / total_balls

# Вывод результата
print("Вероятность выбрать синий шар:", probability_blue)

# + [markdown] id="CqhIHUQHMnz4"
# ## 2

# + [markdown] id="NCpz5Jv3K4ss"
# Задача на теорему сложения вероятностей
#
# Задача: В корзине 4 яблока и 6 апельсинов. Какова вероятность того, что случайно выбранный фрукт будет либо яблоком, либо апельсином?

# + colab={"base_uri": "https://localhost:8080/"} id="WEpoxEKzNRGy" outputId="f6835188-570c-483a-e89f-13cabfcf787a"
apples: int = 4
oranges: int = 6
total_fruits: int = apples + oranges
probability_apples: float = apples / total_fruits
probability_oranges: float = oranges / total_fruits
print("Вероятность, что случайно выбранный фрукт яблоко", probability_apples)
print("Вероятность, что случайно выбранный фрукт апельсин", probability_oranges)

# + [markdown] id="T0aGxIaXMprn"
# ## 3

# + [markdown] id="3eaAf6zRK4s1"
#  задачи на зависимые события
#
# Задача: В коробке находятся 5 синих и 4 красных шарика. Мы случайно вытаскиваем два шарика один за другим без возврата. Какова вероятность того, что первый шар будет синим, а второй — красным?

# + colab={"base_uri": "https://localhost:8080/"} id="mpy8RH52OKys" outputId="b83b2618-84ce-42dd-aea2-cc9acad125f7"
# Определяем количество шаров
blue_balls_: int = 5
red_balls_: int = 4
total: int = blue_balls_ + red_balls_
probability_first_blue: float = blue_balls_ / total
probability_second_red: float = red_balls_ / (total - 1)
probability_first_blue_second_red: float = (
    probability_first_blue * probability_second_red
)
print(round(probability_first_blue_second_red, 2))

# + [markdown] id="x0gttKBmMu4q"
# ## 4

# + [markdown] id="z-mPa-RrQ0KG"
# *Формула полной вероятности*
#
# Формула полной вероятности применяется, когда событие может произойти через несколько взаимно исключающих событий (гипотез), и нам нужно найти вероятность этого события с учётом всех возможных путей его наступления.

# + [markdown] id="Y5w1wZ30K4s2"
# Задача: Предположим, что у нас есть три коробки:
#
#     В первой коробке 3 белых и 2 черных шара.
#     Во второй коробке 1 белый и 1 черный шар.
#     В третьей коробке 4 белых и 3 черных шара.
#
# Случайным образом выбирается одна коробка, и из неё случайно вытаскивают один шар. Какова вероятность того, что этот шар будет белым?

# + [markdown] id="WBo-o8fMEecc"
# Будем считать события B1,B2,B3 выбором урны с соотвествующим номером, а событие A — выбором белого шара. По условию задачи все события выбора урны равновероятны, значит

# + [markdown] id="EHuyClvKEkMd"
# P(B1) = P(B2) = P(B3) = 1/3

# + colab={"base_uri": "https://localhost:8080/"} id="yUnF5q8YDCuE" outputId="b798a3fc-70da-4c3f-b281-b7b498a0eec5"
# Определяем количество шаров
first_basket_white: int = 3
second_basket_white: int = 1
third_basket_white: int = 4

first_basket_black: int = 2
second_basket_black: int = 1
third_basket_black: int = 3

# все события выбора урны равновероятны, значит:
P_B: float = 1 / 3

# Теперь найдём вероятность события A при выборе каждой урны:
P_A1: float = first_basket_white / (first_basket_white + first_basket_black)
P_A2: float = second_basket_white / (second_basket_white + second_basket_black)
P_A3: float = third_basket_white / (third_basket_white + third_basket_black)

# В результате получаем P(A)
P_A: float = P_B * P_A1 + P_B * P_A2 + P_B * P_A3

print("Вероятность того, что этот шар будет белым:", round(P_A, 2))

# Формула Байеса
#
# Формула Байеса позволяет находить условную вероятность гипотезы, исходя из известной вероятности наступившего события. Она позволяет "обновлять" вероятность гипотезы на основании новой информации.
#
# Задача: Предположим, что есть три автомастерские:
#
#     В первой ремонтируют 40% автомобилей, во второй — 35%, в третьей — 25%.
#     Вероятность того, что автомобиль будет отремонтирован правильно, составляет 90% для первой мастерской, 80% для второй и 75% для третьей.
#
# Какова вероятность того, что автомобиль был отремонтирован в первой мастерской, если известно, что ремонт был выполнен правильно?

P_H1: float = 0.4
P_H2: float = 0.35
P_H3: float = 0.25

P_A_H1 = 0.9
P_A_H2 = 0.8
P_A_H3 = 0.75

# найдем полную вероятность события А - ремент выполнен
P_A4: float = (P_H1 * P_A_H1) + (P_H2 * P_A_H2) + (P_H3 * P_A_H3)
# найем условную вероятность H1, если событие А произошло
P_H1_A: float = P_H1 * P_A_H1 / P_A
print(
    f"Вероятность того, что автомобиль был отремонтирован в первой мастерской {round(P_H1_A,2)}",
)
