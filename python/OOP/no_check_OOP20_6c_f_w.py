# %%NBQA-CELL-SEPfaab7c
"Module on oop."


# %%NBQA-CELL-SEPfaab7c
hash(0xED82A8C7)


# %%NBQA-CELL-SEPfaab7c
print(type(list1))  # выводим тип класса


# %%NBQA-CELL-SEPfaab7c
def get_value(
    string: str,
) -> int:  # аннотация типов = type hinting.Задаем параметры функции
    return int(string)


print(get_value("23"))


# %%NBQA-CELL-SEPfaab7c
def sum(
    variable_a: int, variable_b: int
) -> int:  # a: int, b:int - параметры(=фргументы) функции, -> int- что хотим получить
    return variable_a + variable_b


print(sum(5, 4), sum(variable_a=33, variable_b=10))


# %%NBQA-CELL-SEPfaab7c
hash(0xCDFAAED3)


# %%NBQA-CELL-SEPfaab7c
class Body:  #
    size = 100


class Person:

    body = Body()  #

    @property
    def person_name(self):
        return self._name

    @property
    def person_age(self) -> int:
        return self._age
        # return self.get_age()

    def __init__(
        self, person_name: str, person_age: int
    ):  # __inint__ - инициализация самого объекта

        self._name = person_name  # self._person_name - field
        # self._age = age + 100 #
        self._age = person_age

    def get_age(self) -> int:  #
        return self._age  #

    # def  __add__(self, other:"Person"):
    #     # return self._age   + other.get_age()
    #     return f'{self._name}\\{other._name}'

    # def get_drink(self):
    #     if self._age > 18:
    #         print (f"{self._name} Drink!")

    def get_drink(self):
        print("Empty")


# полимовфизм
class USAPerson(Person):  # делаем наследование от класса (Person)
    # @overload # передпределение

    def get_drink(self):  # переопределяем класс
        if self._age > 16:
            print(f"{self._name} Drink in USA!")


class IndianPerson(Person):

    def get_drink(self):  # переопределяем класс
        print(f"{self._name} I don't drink!")


tanya = Person("Tatiana", 17)  # создается инстанс объектв
vita = Person("Vitalina", 15)  #
sanya = Person("Alexander", 21)
ivan = USAPerson(" IVAN", 17)
andrey = IndianPerson("Andrey", 10)


print(vita.get_age())
print(vita.body.size)
print(tanya.body.size)
print(Person.body.size)
# print(tanya + vita)
# print(vita.__add__(tanya))

dir(tanya)
print(tanya._name)
print(
    vita._age
)  # нарушение принципа инкапсуляции тк _age - это для внутреннего пользования!(есть _)
print(vita.person_age)
# print(vita.age+100)
print(vita.get_age())
print(tanya.person_name)
# vita.age = 100 # подает ошибка
sanya.get_drink()
vita.get_drink()
tanya.get_drink()
ivan.get_drink()
andrey.get_drink()
print(andrey.person_name, andrey.person_age)


def test(var_x: Person):
    var_x.get_drink()


test(tanya)
# andrey.test(1)
# andrey.test(1, 2)


# %%NBQA-CELL-SEPfaab7c
class Person:
    # @overload

    @staticmethod
    def test(variable_x: int, variable_y: int):
        print(variable_x + variable_y)

    # @staticmethod
    # def test(variable_x: int):
    #     print(variable_x)


Person.test(2, 4)


# %%NBQA-CELL-SEPfaab7c
# dir(tanya) #  сотрим методы класса для tanya


# %%NBQA-CELL-SEPfaab7c
def print_methods(obj):
    return dir(obj)


print_methods(tanya)  # смотрим методы класса для tanya
