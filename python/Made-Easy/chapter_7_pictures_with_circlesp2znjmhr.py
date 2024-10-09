# %%NBQA-CELL-SEPfaab7c
"Module on the ways to make pictures with circles."


# %%NBQA-CELL-SEPfaab7c
# решение задачи с помощью циклов. Подумаем заново:
# ♦ один цикл будет печатать последовательно 6 рядов;
# ♦ другой цикл будет печатать сами звездочки в рядах.
# row =6 # количество строк или высота треугольника


def pattern_T(row):
    for i in range(0, row):  # цикл для перебора строк
        for j in range(0, i + 1):  # цикл для перебора в диапазоне
            # от 0 до 1 + номер строки
            print("* ", end="")  # вывод звездочек в строке
        print("")  # переход на следующую строку


pattern_T(6)


# %%NBQA-CELL-SEPfaab7c
def pattern_T_inverse(n):
    spaces = (n - 1) * 2
    for i in range(0, n):
        for j in range(0, spaces):
            print(" ", end="")
        for j in range(0, i + 1):
            print("* ", end="")
        spaces = spaces - 2
        print("")


pattern_T_inverse(6)


# %%NBQA-CELL-SEPfaab7c
def pattern_RT(n):
    spaces = n - 1
    for row in range(0, n):
        for space in range(0, spaces):
            print(" ", end="")
        for star in range(0, row + 1):
            print("* ", end="")
        spaces = spaces - 1
        print("")


pattern_RT(6)


# %%NBQA-CELL-SEPfaab7c
# Picture 1


def pattern_RV(n):
    dif = n
    spaces = 1

    for row in range(n, 0, -1):
        for space in range(0, spaces):
            print(" ", end="")

        for star in range(0, row):
            print("* ", end="")

        spaces += 1
        print("")


pattern_RV(6)


# %%NBQA-CELL-SEPfaab7c
def pattern_united(n):
    spaces = n - 1
    for row in range(0, n):
        for space in range(0, spaces):
            print(" ", end="")
        for star in range(0, row + 1):
            print("* ", end="")
        spaces = spaces - 1
        print("")

    dif = n
    spaces = 1

    for row in range(n, 0, -1):
        for space in range(0, spaces):
            print(" ", end="")

        for star in range(0, row):
            print("* ", end="")

        spaces += 1
        print("")


pattern_united(6)


# %%NBQA-CELL-SEPfaab7c
# Picture 3


def pattern_un(n):
    spaces = n - 1
    for row in range(0, n):
        for space in range(0, spaces):
            print(" ", end="")
        for star in range(0, row + 1):
            print("* ", end="")
        spaces = spaces - 1
        print("")

    dif = n
    spaces = 1

    for row in range(n - 1, 0, -1):
        for space in range(0, spaces):
            print(" ", end="")

        for star in range(0, row):
            print("* ", end="")

        spaces += 1
        print("")


pattern_un(6)


# %%NBQA-CELL-SEPfaab7c
# Picture 6


def triangle(row):
    # Верхний треугольник
    for i in range(row, 0, -1):  # от row до 0 в обратном порядке
        # Вывод пробелов
        for space in range(row - i):
            print(" ", end="")

        # Вывод звездочек
        for star in range(i):
            print("* ", end="")

        print("")  # Переход на новую строку

    # Нижний треугольник
    for i in range(1, row + 1):  # проходим ряд от 1 до row+1
        # Вывод пробелов
        for space in range(row - i):  # к-во пробелов от ряд - i
            print(" ", end="")

        # Вывод звездочек
        for star in range(i):  #
            print("* ", end="")

        print("")  # Переход на новую строку


triangle(6)


# %%NBQA-CELL-SEPfaab7c
def pattern_RV(n):
    dif = n
    spaces = 1

    for row in range(n, 0, -1):
        for space in range(0, spaces):
            print(" ", end="")

        for star in range(0, row):
            print("* ", end="")

        spaces += 1
        print("")


pattern_RV(6)


# %%NBQA-CELL-SEPfaab7c
# Picture 4


def pattern_un(n):
    spaces = n - 1
    for row in range(0, n):
        for space in range(0, spaces):
            print("-", end="")
        for star in range(0, row + 1):
            print("* ", end="")
        spaces = spaces - 1
        print("")

    dif = n
    spaces = 1

    print()
    print()

    for row in range(n, 0, -1):
        for space in range(0, spaces):
            print("-", end="")

        for star in range(0, row):
            print("* ", end="")

        spaces += 1
        print("")


pattern_un(6)


# %%NBQA-CELL-SEPfaab7c
print("* " * 6)


# %%NBQA-CELL-SEPfaab7c
def pattern_RT(n):
    spaces = n - 1
    for row in range(0, n):
        for space in range(0, spaces):
            print(" ", end="")
        for star in range(0, row + 1):
            print("* ", end="")
        spaces = spaces - 1
        print("")


pattern_RT(6)


# %%NBQA-CELL-SEPfaab7c
row = 6
for i in range(row, 0, -1):  # диапазон
    for j in range(0, i):
        print("* ", end="")
    print("")


# %%NBQA-CELL-SEPfaab7c
row = 6
for i in range(0, row + 1):  # диапазон
    for j in range(0, i):
        print("* ", end="")
    print("")


# %%NBQA-CELL-SEPfaab7c
row = 11
peak = row // 2 + 1

for i in range(0, peak):
    for j in range(0, i):
        print("* ", end="")
    print("")

for i in range(peak, 0, -1):
    for j in range(0, i):
        print("* ", end="")
    print("")


# %%NBQA-CELL-SEPfaab7c
# Picture 2

for i in range(0, 6 + 1):
    for j in range(0, i):
        print("* ", end="")
    print("")
print()
print()
for i in range(6, 0, -1):
    for j in range(0, i):
        print("* ", end="")
    print("")


# %%NBQA-CELL-SEPfaab7c
row = 6
for i in range(0, row + 1):
    for j in range(0, i):
        print(i, end=" ")  # вывод чисел по строкам
    print("")


# %%NBQA-CELL-SEPfaab7c
row = 6
for i in range(row + 1):
    for j in range(i):
        print(i, end="-")
    print("@")


# %%NBQA-CELL-SEPfaab7c
def numpattern2(n):
    for i in range(0, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print("")


numpattern2(6)


# %%NBQA-CELL-SEPfaab7c
def numpattern3(n):
    num = 1
    for i in range(n, 0, -1):
        for j in range(0, i):
            print(num, end=" ")
        num = num + 1
        print("")


numpattern3(6)


# %%NBQA-CELL-SEPfaab7c
row = 6
for i in range(0, row + 1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print("")


# %%NBQA-CELL-SEPfaab7c
row = 6
for i in range(0, row + 1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print("")


# %%NBQA-CELL-SEPfaab7c
row = 6
for i in range(0, row + 1):
    for j in range(i, 0, -1):
        print(j**2, end=" ")
    print("")


# %%NBQA-CELL-SEPfaab7c
def numpattern6(n):
    spaces = n - 1
    num_count = 1
    for row in range(1, n + 1):
        for i in range(0, spaces):
            print(" ", end="")
        for num in range(0, num_count):
            print(row, end=" ")
        print("")
        spaces = spaces - 1
        num_count = num_count + 1

    spaces = 1
    num_count = n - 1
    for row in range(n - 1, 0, -1):
        for i in range(0, spaces):
            print(" ", end="")
        for num in range(0, num_count):
            print(row, end=" ")
        spaces = spaces + 1
        num_count = num_count - 1
        print("")


numpattern6(6)


# %%NBQA-CELL-SEPfaab7c
def numpattern7(n):

    spaces = n
    num_count = 1
    for row in range(0, n + 1):
        for i in range(0, spaces):
            print(" ", end="")
        for num in range(1, num_count):
            print(num, end=" ")
        print("")
        spaces = spaces - 1
        num_count = num_count + 1

    spaces = 1
    num_count = n
    for row in range(n, 0, -1):
        for i in range(0, spaces):
            print(" ", end="")
        for num in range(1, num_count):
            print(num, end=" ")
        spaces = spaces + 1
        num_count = num_count - 1
        print("")


numpattern7(6)


# %%NBQA-CELL-SEPfaab7c
row = 6
spaces = row - 1
num_count = 1

for i in range(0, row):
    for j in range(0, spaces):
        print(" ", end="")
    for num in range(0, num_count):
        print(num, end="")
    print("")
    spaces = spaces - 1
    num_count = num_count + 1

spaces = 1
num_count = row - 1
for i in range(row, 0, -1):
    for j in range(0, spaces):
        print(" ", end="")
    for num in range(0, num_count):
        print(num, end="")
    spaces = spaces + 1
    num_count = num_count - 1
    print("")
