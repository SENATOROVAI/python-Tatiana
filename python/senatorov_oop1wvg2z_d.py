# %%NBQA-CELL-SEPfaab7c
class Cat:
    # реализована инкопсуляция.Добираемся через метод
    __hello = "hello"

    def get_hello():
        return Cat.__hello


# %%NBQA-CELL-SEPfaab7c
Cat.__hello  #


# %%NBQA-CELL-SEPfaab7c
Cat.get_hello()


# %%NBQA-CELL-SEPfaab7c
print(Cat.get_hello())


# %%NBQA-CELL-SEPfaab7c
class CatObject:
    """
    void method  - метод без опертаора return

    результирующий метод - метод с оператором return

    """

    def __init__(self, name):
        # __hello = 'hello'
        # senatorov = 'hello'
        # hel_sen = 'Hello Senatorov'
        # hel_tat  = 'Hello Tatyana'

        self.name = name

    def get_hello(self):
        return CatObject.__hello

    def hello_all(self, name):
        return f"Hello {name}"

    def hello_name(self):
        return f"Hello {self.name}"


# %%NBQA-CELL-SEPfaab7c
ruslan = CatObject("Senatorov")
ruslan.hello_name()


# %%NBQA-CELL-SEPfaab7c
senatorov = CatObject()
senatorov.hello_all("Tatyana")


# %%NBQA-CELL-SEPfaab7c
kitty = CatObject()


# %%NBQA-CELL-SEPfaab7c
kitty.senatorov


# %%NBQA-CELL-SEPfaab7c
# kitty.get_hello(kitty)# неявно интерпретатор передал
# в метод имя объекта kitty
kitty.get_hello()


# %%NBQA-CELL-SEPfaab7c
dir(kitty)  #  в dir нет атрибута __hello тк он инкапсултирован.
# '_CatObject__hello' - прямое обращение к инкаппсулированнуму методу


# %%NBQA-CELL-SEPfaab7c
kitty.__class__
