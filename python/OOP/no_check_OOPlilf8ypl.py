# %%NBQA-CELL-SEPfaab7c
class Bill:
    # with __init__ we create a class abiblity
    def __init__(self):  # method init
        self.money = 0  # class abiblity

    # with def we create class methods
    def add(self, count):
        self.money += count

    def withdraw(self, count):
        if self.money > count:
            self.money -= count


# %%NBQA-CELL-SEPfaab7c
bill = (
    Bill()
)  # Создаем объект класса Bill=объявляем переменную = операция инстанцирования объекта
bill.add(100)
bill.withdraw(25)
print(bill.money)


# %%NBQA-CELL-SEPfaab7c
# list_numbers: list = [] #
num_list: list = list()  # создаем объект кла snake-caseа
num_list.append(2)  #


# %%NBQA-CELL-SEPfaab7c
dir(list)  # выводит имена атрибутов и методов класса или объекта


# %%NBQA-CELL-SEPfaab7c
type(num_list)  # экзкмпляр=чайлд класса лист показвает типа даных или имя класса


# %%NBQA-CELL-SEPfaab7c
class List_:  # pascal-case(ListNumbers) наследуемся явно от класса. Указать класс в ()
    """Все классы наследуются от класса object, неявно. Визуально не видно"""

    NAME = "IRINA"
    __FAMILY_NAME = "IVANOVA"  # incapsulated method

    def __init__(self):

        self.name = "kypena"  # создаем атрибут класса

    def get_name(self):
        return List_.NAME

    def get_family_name(self):
        return List_.__FAMILY_NAME


# print(List_.__name) #
# print(List_.get_name()) #

object_list = List_()
# print(object_list.name)

# print(object_list.get_name())
# print(object_list.get_family_name()) # we reached incapsulayed attribute via method
# print(object_list.__FAMILY_NAME) # did not work as this attribute as incapsulated
print(object_list._List___FAMILY_NAME)  # we reached incapsulayed attribute via method


# %%NBQA-CELL-SEPfaab7c
object


# %%NBQA-CELL-SEPfaab7c
dir(List_)  # выводим атрибуты и метгоды класса


# %%NBQA-CELL-SEPfaab7c
def append(self, __object: _T) -> None: ...
