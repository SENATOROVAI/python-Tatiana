# %%NBQA-CELL-SEPfaab7c
"Module on python.Builtins(=built-in objects) , dunder methods."


# %%NBQA-CELL-SEPfaab7c
# !pip install numpy
import numpy as np


# %%NBQA-CELL-SEPfaab7c
lst1: list = []  # создание экземпляра класса list
lst2: list = []  # [] - это объект


# %%NBQA-CELL-SEPfaab7c
type(lst1)  #


# %%NBQA-CELL-SEPfaab7c
dir(lst1)


# %%NBQA-CELL-SEPfaab7c
list  # ctrl  - провалиться в класс


# %%NBQA-CELL-SEPfaab7c
for i in range(11):
    lst1.append(i)
    lst2.append(i)


# %%NBQA-CELL-SEPfaab7c
lst1, lst2


# %%NBQA-CELL-SEPfaab7c
id(lst1)
id(lst2)


# %%NBQA-CELL-SEPfaab7c
lst1 is lst2


# %%NBQA-CELL-SEPfaab7c
lst_copy = lst1  # 2 количество ссылок. Garbage collector не может уничтожить объект, тк на него ссылается вторая переменная
del lst1
del lst_copy  # удаление обоих переменных удаяем их ссылки на объект


# %%NBQA-CELL-SEPfaab7c
lst1


# %%NBQA-CELL-SEPfaab7c
# Области видимости:

# (built-in) — область системных имен

# global # — область модуля. Модуль - файл с расшмрением .py


def outer():
    # enclosed — область функции-обёртки = ближайшая область видимости
    def inner():
        # local — область внутри функции
        pass


# %%NBQA-CELL-SEPfaab7c
class MyClass:
    def __init__(self, __param):  # конструктор класса вызывается автоматом
        self.__param = (
            __param  # создаем свойство __param, нужен для инициализации данных в классе
        )

    def print_param(self) -> None:
        print(self.__param)


# %%NBQA-CELL-SEPfaab7c
name = MyClass("Kate")  # создание экземпляра класса=объекта класс
# автоматически вызывается конструктор класс. Нужен для инициализации данных в класса


# %%NBQA-CELL-SEPfaab7c
name.print_param()  # обращение к методу класса


# %%NBQA-CELL-SEPfaab7c
dir(name)


# %%NBQA-CELL-SEPfaab7c
dir(np)


# %%NBQA-CELL-SEPfaab7c
arr = np.array(
    [1, 2, 3], dtype="int32"
)  # под каждый тип данных выделяется опрееленный тип данных.Numpy работает со строгим типом данных
arr


# %%NBQA-CELL-SEPfaab7c
arr2 = np.array([1.0, 2.0, 3.0])
print(arr2, type(arr2))
print(arr2.ndim)  # количесво измерений =глубина
