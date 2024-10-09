# %%NBQA-CELL-SEPfaab7c
"Module on flow statements."


# %%NBQA-CELL-SEPfaab7c
# if
# if условие:
#     код блока if
# конец блока if


# %%NBQA-CELL-SEPfaab7c
# Оператор if-else
# нужно что-то сделать, если условие if не выполни­лось,
# т. е. оказалось ложно. Для этого у нас есть оператор if-else

# if условие:
#   код блока if
# else:
#   код блока else


# %%NBQA-CELL-SEPfaab7c
num = int(input("Please enter an integer: "))
if num < 0:
    print("Negative Number")
elif num == 0:
    print("Zero")
elif num == 1:
    print("Single")
else:
    print("More")


# %%NBQA-CELL-SEPfaab7c
name = "Petin Kate"
basic_salary = int(input("Salatry of {} is: ".format(name)))
city_class = input("{} lives in a city class:".format(name))

if city_class == ("a" or "A"):
    hra = (basic_salary * 30) / 100
elif city_class == ("b" or "B"):
    hra = (basic_salary * 20) / 100
elif city_class == ("c" or "C"):
    hra = (basic_salary * 10) / 100

print("Compensation for the rent for {} will be: {}".format(name, hra))


# %%NBQA-CELL-SEPfaab7c
# for переменная in последовательность:
#   код блок for


# %%NBQA-CELL-SEPfaab7c
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    print(i)
else:
    print("this is end of the code!")


# %%NBQA-CELL-SEPfaab7c
# range() создает итерируемый объект
print(range(-10, -100, -30))  # просто выводите диапазонсок из итерируемого объекта
list(range(5))  # создвет спи


# %%NBQA-CELL-SEPfaab7c
num = 10
# присвоение значений переменным
sum = 0
count = 1
while count <= num:
    sum = sum + count
    count = count + 1
# обновление счетчика146
print("The sum is", sum)


# %%NBQA-CELL-SEPfaab7c
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    print(i)
    break
else:
    print("this is end of the code!")
print("this line is outside the loop")
# оператор break остановил цикл for и не перевел его на
# следующую итерацию и про­пустил блок else.


# %%NBQA-CELL-SEPfaab7c
# Присмотритесь внимательно: здесь блок else относится к циклу for,
# а не к опера
# тору if
for i in range(2, 10):
    for x in range(2, n):
        if i % x == 0:
            print(i, "equals", x, i // x)
            break
    else:
        # цикл прерывается, не найдя делителя
        print(i, 2, "is a prime number")


# %%NBQA-CELL-SEPfaab7c
for alphabet in "python":
    if alphabet == "t":
        continue
    print(alphabet)
print("The end")


# %%NBQA-CELL-SEPfaab7c
for num in range(2, 10):
    if num % 2 == 0:
        # четное число
        print("Found an even number", num)
        continue
    print("Found a number", num)


# %%NBQA-CELL-SEPfaab7c
class MyEmptyClass:
    pass


# %%NBQA-CELL-SEPfaab7c
# a) # код ничего не выведет тк не попадет в блок кода if
num = 50
if num >= 100:
    print("Value of num is {}".format(num))


# %%NBQA-CELL-SEPfaab7c
# б) # выведет то что в print
num = 90
if num <= 100:
    print("Value of num is {}".format(num))


# %%NBQA-CELL-SEPfaab7c
# в) выведет Value of num is 50
num = 50
if num >= 10:
    print("Value of num is {}".format(num))
else:
    print("Value of num is less than 10")


# %%NBQA-CELL-SEPfaab7c
# г) Value of num is less than 10

num = 22
if num >= 10:
    print("Value of num is {}".format(num))
else:
    print("Value of num is less than 10")


# %%NBQA-CELL-SEPfaab7c
# д) вывод: 0,1,2,3,4

num = 0
while num < 5:
    print(num)
    num += 1


# %%NBQA-CELL-SEPfaab7c
# e) 5, 10, 15 ,20

for i in range(5, 25, 5):
    print(i)


# %%NBQA-CELL-SEPfaab7c
# 1. Трейдер хочет, чтобы программа проверяла, получил ли он прибыль или убы­
# ток по сделке. Напишите программу, в которой с клавиатуры вводится цена по­
# купки и продажи, а в ответ программа сообщает, получил ли трейдер прибыль
# или убыток. Программа также должна рассчитать сумму прибыли или убытка.

purchase_price, sale_price = map(float, input().split())
difference = sale_price - purchase_price
if difference > 0:
    print("Got profit:", difference)
else:
    print("Got loss:", difference)


# %%NBQA-CELL-SEPfaab7c
# 2. Напишите программу, которая проверяет, является ли год, введенный с клавиа­
# туры, високосным.

year_to_check = int(input())
if year_to_check % 4 != 0:
    print("Not even year")
elif year_to_check % 100 == 0:
    if year_to_check % 400 == 0:
        print("Even year")
    else:
        print("Not even year")
else:
    print("Not even year")


# %%NBQA-CELL-SEPfaab7c
# 3. Трое сотрудников, Самир, Правин и Мохит, вводят свой опыт работы с клавиа­
# туры. Напишите программу, которая определяет наиболее и наименее опытного
# из них.

# Ввод опыта работы сотрудников
samir_experience = int(input("Введите опыт работы Самира: "))
pravin_experience = int(input("Введите опыт работы Правина: "))
mohit_experience = int(input("Введите опыт работы Мохита: "))

# Определение наиболее и наименее опытного сотрудника
most_experienced = max(samir_experience, pravin_experience, mohit_experience)
least_experienced = min(samir_experience, pravin_experience, mohit_experience)

# Вывод результатов
if samir_experience == most_experienced:
    print("Самир является наиболее опытным сотрудником.")
if pravin_experience == most_experienced:
    print("Правин является наиболее опытным сотрудником.")
if mohit_experience == most_experienced:
    print("Мохит является наиболее опытным сотрудником.")

if samir_experience == least_experienced:
    print("Самир является наименее опытным сотрудником.")
if pravin_experience == least_experienced:
    print("Правин является наименее опытным сотрудником.")
if mohit_experience == least_experienced:
    print("Мохит является наименее опытным сотрудником.")


# %%NBQA-CELL-SEPfaab7c
# 4. Сумма трех углов треугольника составляет 180°. Напишите программу, которая
# проверяет, является ли фигура треугольником, если в качестве входных данных
# вводятся три угла.
angle_a, angle_b, angle_c = map(int, input().split())
if angle_a + angle_b + angle_c == 180:
    print("Triangle")
else:
    print("Not a triangle")


# %%NBQA-CELL-SEPfaab7c
# 5. Даны три угла треугольника. Напишите программу, которая проверит, является
# ли он прямоугольным (один из углов должен составлять 90°).

# Ввод углов треугольника
angle_a, angle_b, angle_c = map(int, input().split())

# Проверка на прямоугольный треугольник
if angle_a == 90 or angle_b == 90 or angle_c == 90:
    print("Right triangle")
else:
    if angle_a + angle_b + angle_c == 180 and (
        angle_a + angle_b == 90 or angle_a + angle_c == 90 or angle_b + angle_c == 90
    ):
        print("Right triangle")
    else:
        print("Not right triangle")


# %%NBQA-CELL-SEPfaab7c
# 6. Сколько разных трехзначных чисел можно получить, используя цифры 1, 2 и 3
# в разных позициях? Напишите программу для генерации всех таких чисел (под­
# сказка: используйте цикл for).

count = 0

for i in range(1, 4):  # Первая цифра (единицы)
    for j in range(1, 4):  # Вторая цифра (десятки)
        for k in range(1, 4):  # Третья цифра (сотни)
            if i != j and j != k and i != k:  # Условие для различных цифр
                number = i * 100 + j * 10 + k
                print(number)
                count += 1
print(count)


# %%NBQA-CELL-SEPfaab7c
# 7. Напишите код для вывода таблицы умножения любого заданного числа.

number = int(input())

for i in range(1, 11):
    print(f"{number}*{i}={number*i}")


# %%NBQA-CELL-SEPfaab7c
# 8. Напишите программу для вывода всех простых чисел от 1 до 500.
# https://habr.com/ru/articles/122538/
# for i in range(,501):

# создаем пустой список для хранения простых чисел
lst = []
# в k будем хранить количество делителей
k = 0
# пробегаем все числа от 2 до N
for i in range(1, 500 + 1):
    # пробегаем все числа от 2 до текущего
    for j in range(2, i):
        # ищем количество делителей
        if i % j == 0:
            k = k + 1
    # если делителей нет, добавляем число в список
    if k == 0:
        lst.append(i)
    else:
        k = 0
# выводим на экран список
print(lst)


# %%NBQA-CELL-SEPfaab7c
# 9. Выведите все числа, кратные 9, которые меньше 300 (подсказка: вы можете ис­пользовать функцию range о).

for i in range(1, 301):  # проходимся по всем числам от 1 до 300
    if i % 3 == 0:
        print(i)


# %%NBQA-CELL-SEPfaab7c
# 10. Машина в течение срока службы приносит годовой доход в размере 200 000 руб.
# Сама она стоит 1 000 000 руб. в момент покупки и продается за 250 000 руб.
# при утилизации. Вложив ту же сумму в другие инвестиционные инструменты,
# можно заработать 8 % годовых. Каков минимальный срок службы машины, при
# котором она станет более привлекательной по сравнению с альтернативными
# инвестициями?


# %%NBQA-CELL-SEPfaab7c
def calculate_profit(years):
    total_revenue_machine = 200000 * years  # общий доход от машины за год
    initial_cost = 1000000
    salvage_value = 250000
    revenue_investment = (
        initial_cost * (1 + 0.08) ** years
    )  # доход от инвестиций с учетом ставки и сроков  c сложный процент

    profit_machine = total_revenue_machine - initial_cost + salvage_value
    profit_investment = revenue_investment - initial_cost

    return profit_machine - profit_investment


years = 1
while calculate_profit(years) <= 0:
    years += 1
print(f"Минимальный срок окупаемости машины : {years} лет")
