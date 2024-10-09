# %%NBQA-CELL-SEPfaab7c
"Module on chapter 3 python basics."


# %%NBQA-CELL-SEPfaab7c
variable_p = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
print(p)


# %%NBQA-CELL-SEPfaab7c
variable_l = 1 * 2 * 3 + 7 + 8 + 9
print(variable_l)


# %%NBQA-CELL-SEPfaab7c
footballer = ["MESSI", "NEYMAR", "SUAREZ"]
print(footballer)


# %%NBQA-CELL-SEPfaab7c
variable_x = {1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9}
print(variable_x)


# %%NBQA-CELL-SEPfaab7c
flag = 2
ropes = 3
pole = 4
print(flag, ropes, pole)


# %%NBQA-CELL-SEPfaab7c
# "Hello World!"


# %%NBQA-CELL-SEPfaab7c
print("Hello World!")


# %%NBQA-CELL-SEPfaab7c
variable_a = 0
variable_b = 1
while variable_a < 10:
    print(variable_a)
    variable_a, variable_b = variable_b, variable_a + variable_b


# %%NBQA-CELL-SEPfaab7c
variable_a, variable_b = 0, 1  # множественное присваивание: переменные а и ь
# одновременно получают значения о и 1

while variable_a < 15:
    print(variable_a)
    variable_a, variable_b = variable_b, variable_a + variable_b


# %%NBQA-CELL-SEPfaab7c
letter_a = 5
letter_b = 6
product_ab = 5 * 6
print(
    "when {} is multiplied by {}, the result is {}".format(
        letter_a, letter_b, product_ab
    )
)


# %%NBQA-CELL-SEPfaab7c
print("      /|")
print("     / |")
print("    /  |")
print("   /   |")
print("  /    |")
print(" /     |")
print("/______|")


# %%NBQA-CELL-SEPfaab7c
# 1. Напишите программу, в которой бы соединялись ваши имя и фамилия. Между
# ними должен быть пробел.
name = "Nick"
surname = "Popov"
print(name + " " + surname)


# %%NBQA-CELL-SEPfaab7c
# 2. Прямоугольник имеет длину 1 (англ, буква l) и высоту h. Напишите код для вы­
# числения площади прямоугольника с высотой 8 и длиной 23. В коде должно
# быть присвоение значений переменным 1 и h, чтобы один и тот же код можно
# было использовать повторно. Для вычисления площади прямоугольника нужно
# его длину умножить на высоту.
height = 8
lenght = 23
square = height * lenght
print(square)


# %%NBQA-CELL-SEPfaab7c
# 3. Чему равен квадрат числа 32 и куб числа 27? Напишите оператор, который от­
# ветит на этот вопрос.
print(32**2, 27**2)


# %%NBQA-CELL-SEPfaab7c
# 4. Напишите приведенное ниже уравнение на Python. Присвойте числовые значе­
# ния переменным и вычислите результат.
# (а + b)^2 = а^2 + b^2 + 2аЬ
variable_a, variable_b = 4, 5
square_sum = variable_a**2 + variable_b**2 + variable_a * variable_b
print(square_sum)


# %%NBQA-CELL-SEPfaab7c
# 5. Найдите длину своего имени, написав однострочный код на Python.
my_name = "Tatiana"
print(len(name))


# %%NBQA-CELL-SEPfaab7c
# 6. Нарисуйте прямоугольник, используя функцию print ().
print(" _________")
print("|         |")
print("|         |")
print("|_________|")


# %%NBQA-CELL-SEPfaab7c
# 7. Нарисуйте букву «Р» с помощью простейшей геометрии и функции
# print ().
print("  ___")
print(" |   \\")  # экранирование /
print(" |___/")
print(" |")
print(" |")


# %%NBQA-CELL-SEPfaab7c
# 8. Создайте переменную Name и присвойте ей свое имя. Переменной Аge присвойте
# свой возраст. Затем напишите оператор print(), который выведет текст «меня
# зовут Name, а мой возраст - Аде», с подставленными значениями ваших перемен­
# ных. Значения Name и Аде должны быть строкой и числом соответственно
name = "Fiona"
age = 25
print("меня зовут {}, а мой возраст -{}".format(name, age))


# %%NBQA-CELL-SEPfaab7c
# 9. Исправьте синтаксическую ошибку в следующих строках кода:
words = ["cat", "window", "defenestrate"]
for word in words:
    print(word, len(word))


# %%NBQA-CELL-SEPfaab7c
# 10. Исправьте синтаксическую ошибку в следующих строках кода:
# letter_a, letter_b = 0, 1
# while letter_a < 15:
#     print(letter_a, end=',')

letter_a, letter_b = 0, 1
while letter_a < 15:
    print(letter_a, end=",")
    letter_a += 3
