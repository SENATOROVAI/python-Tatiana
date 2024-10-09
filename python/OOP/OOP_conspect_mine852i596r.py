# %%NBQA-CELL-SEPfaab7c
class CatClass:

    type_ = "cat"

    def __init__(self, color):

        self.color = color
        self.type_ = "cat"
        self.__type_ = "my cat"

    def meow(self):
        for i in range(3):
            print("Meow")

    def info(self):
        print(self.color, self.type_)


# %%NBQA-CELL-SEPfaab7c
Matroskin = CatClass("gray")


# %%NBQA-CELL-SEPfaab7c
Matroskin.color


# %%NBQA-CELL-SEPfaab7c
Matroskin.meow()


# %%NBQA-CELL-SEPfaab7c
Matroskin.info()


# %%NBQA-CELL-SEPfaab7c
# Matroskin.__type_ = 'tiger'
Matroskin._CatClass__type_
# читерство! Обращение к инкапсулированному атрибуту через
# класс с нижним подчеркиванием пред ним


# %%NBQA-CELL-SEPfaab7c
Matroskin = CatClass("gray")
# теперь при вызове этого атрибута Питон выдаст ошибку
# Matroskin.__type_


# %%NBQA-CELL-SEPfaab7c
Matroskin.type_ = "dog"
Matroskin.info()
# изменен атрибут чрез экземпляр класса
CatClass.type_  # вывод атрибута класса


# %%NBQA-CELL-SEPfaab7c
kitty = CatClass("white")
kitty.type_


# %%NBQA-CELL-SEPfaab7c
# создадим класс Animal
class Animal:

    # пропишем метод .__init__() с двумя параметрами: вес (кг) и длина (см)
    def __init__(self, weight, length):

        # поместим аргументы этих параметров в соответствующие переменные
        self.weight = weight
        self.length = length

    # объявим методы .eat()
    def eat(self):
        print("Eating")

    # и .sleep()
    def sleep(self):
        print("Sleeping")


# %%NBQA-CELL-SEPfaab7c
# создадим класс Bird
# родительский класс Animal пропишем в скобках
class Bird(Animal):

    # внутри класса Bird объявим новый метод .move()
    def move(self):

        # для птиц .move() будет означать "летать"
        print("Flying")


# %%NBQA-CELL-SEPfaab7c
# создадим объект pigeon и передадим ему значения веса и длины
pigeon = Bird(0.3, 30)  # вес и длина из класса Animal
pigeon.weight, pigeon.length, pigeon.eat(), pigeon.move()


# %%NBQA-CELL-SEPfaab7c
# снова создадим класс Bird - дочерний от Animal
class Bird(Animal):

    # в метод .__init__() добавим параметр скорости полета (км/ч)
    def __init__(self, weight, length, flying_speed):

        # с помощью функции super() вызовем метод .__init__() родительского класса Animal
        super().__init__(weight, length)
        self.flying_speed = flying_speed

    # вновь пропишем метод .move()
    def move(self):
        print("Flying")


# %%NBQA-CELL-SEPfaab7c
# вновь создадим объект pigeon класса Bird, но уже с тремя параметрами
pigeon = Bird(0.3, 30, 100)


# %%NBQA-CELL-SEPfaab7c
# вызовем как унаследованные, так и собственные атрибуты класса Bird
pigeon.weight, pigeon.length  # атрибуты родительского класса
# pigeon.flying_speed # атрибуты дочеренего класса


# %%NBQA-CELL-SEPfaab7c
# вызов метода род класса
pigeon.sleep()
# вызов метода дочерн класса
pigeon.move()


# %%NBQA-CELL-SEPfaab7c
# создадим подкласс Flightless класса Bird
class Flightless(Bird):

    # метод .__init__() этого подкласса "стирает" .__init__() родительского класса
    def __init__(self, running_speed):  # принимает 1 параметр

        # таким образом, у нас остается только один атрибут
        self.running_speed = running_speed

    # кроме того, результатом метода .move() будет 'Running'
    def move(self):
        print("Running")


# %%NBQA-CELL-SEPfaab7c
# создадим объект ostrich класса Flightless
ostrich = Flightless(60)  # 60 - running_speed
# посмотрим на значение атрбута скорости
ostrich.running_speed


# %%NBQA-CELL-SEPfaab7c
print("Переопределенный метод move: ", ostrich.move())
print("Родительский метод eat: ", ostrich.eat())


# %%NBQA-CELL-SEPfaab7c
class Fish:
    def swim(self):
        print("Swim")


# %%NBQA-CELL-SEPfaab7c
class Bird:
    def fly(self):
        print("Fly")


# %%NBQA-CELL-SEPfaab7c
# теперь создадим класс-потомок и передаем в него 2 род класса
class SwimmingBird(Bird, Fish):
    pass


# %%NBQA-CELL-SEPfaab7c
duck = SwimmingBird()
duck.fly(), duck.swim()


# %%NBQA-CELL-SEPfaab7c
# создадим класс котов
class DogClass:

    # определим атрибуты клички, типа и цвета шерсти
    def __init__(self, name, color):
        self.name = name
        self._type_ = "собака"
        self.color = color

    # создадим метод .info() для вывода этих атрибутов
    def info(self):
        print(f"Меня зовут {self.name}, я {self._type_}, цвет моей шерсти {self.color}")

    # и метод .sound(), показывающий, что коты умеют мяукать
    def sound(self):
        print("Я умею лаять")


# %%NBQA-CELL-SEPfaab7c
# создадим класс котов
class CatClass:

    # определим атрибуты клички, типа и цвета шерсти
    def __init__(self, name, color):
        self.name = name
        self._type_ = "кот"
        self.color = color

    # создадим метод .info() для вывода этих атрибутов
    def info(self):
        print(f"Меня зовут {self.name}, я {self._type_}, цвет моей шерсти {self.color}")

    # и метод .sound(), показывающий, что коты умеют мяукать
    def sound(self):
        print("Я умею мяукать")


# %%NBQA-CELL-SEPfaab7c
cat = CatClass("Черныш", "черный")
dog = DogClass("Пушок", "рыжий")


# %%NBQA-CELL-SEPfaab7c
for animal in (cat, dog):
    animal.info()  # обращение к методу экземпляра
    animal.sound()
    print()


# %%NBQA-CELL-SEPfaab7c
# нашему классу понадобится Numpy
import numpy as np

# создадим класс SimpleLinearRegression


class SimpleLinearRegression:

    # в методе .__init__() объявим переменные наклона и сдвига
    def __init__(self):
        self.slope_ = None
        self.intercept_ = None

    # создадим метод .fit()
    def fit(self, X, y):

        # найдем среднее значение X и y
        X_mean = self.find_mean(X)
        y_mean = self.find_mean(y)

        # объявим переменные для числителя и знаменателя
        numerator, denominator = 0, 0

        # в цикле пройдемся по данным
        for i in range(len(X)):

            # вычислим значения числителя и знаменателя по формуле выше
            numerator += (X[i] - X_mean) * (y[i] - y_mean)
            denominator += (X[i] - X_mean) ** 2

        # найдем наклон и сдвиг
        slope_ = numerator / denominator
        intercept_ = y_mean - slope_ * X_mean

        # сохраним получившиеся коэффициенты в виде атрибутов
        self.slope_ = slope_
        self.intercept_ = intercept_

    # метод .predict() просто умножит через скалярное произведение
    # вектор данных на наклон и прибавит сдвиг
    def predict(self, X):
        # на выходе мы получим вектор прогнозных значений
        return np.dot(self.slope_, X) + self.intercept_

    # служебный метод: расчет среднего
    def find_mean(self, nums):
        return sum(nums) / len(nums)


# %%NBQA-CELL-SEPfaab7c
# возьмем данные роста и обхвата шеи
X = np.array(
    [
        1.48,
        1.49,
        1.49,
        1.50,
        1.51,
        1.52,
        1.52,
        1.53,
        1.53,
        1.54,
        1.55,
        1.56,
        1.57,
        1.57,
        1.58,
        1.58,
        1.59,
        1.60,
        1.61,
        1.62,
        1.63,
        1.64,
        1.65,
        1.65,
        1.66,
        1.67,
        1.67,
        1.68,
        1.68,
        1.69,
        1.70,
        1.70,
        1.71,
        1.71,
        1.71,
        1.74,
        1.75,
        1.76,
        1.77,
        1.77,
        1.78,
    ]
)
y = np.array(
    [
        29.1,
        30.0,
        30.1,
        30.2,
        30.4,
        30.6,
        30.8,
        30.9,
        31.0,
        30.6,
        30.7,
        30.9,
        31.0,
        31.2,
        31.3,
        32.0,
        31.4,
        31.9,
        32.4,
        32.8,
        32.8,
        33.3,
        33.6,
        33.0,
        33.9,
        33.8,
        35.0,
        34.5,
        34.7,
        34.6,
        34.2,
        34.8,
        35.5,
        36.0,
        36.2,
        36.3,
        36.6,
        36.8,
        36.8,
        37.0,
        38.5,
    ]
)


# %%NBQA-CELL-SEPfaab7c
# создадим объект класса SimpleLinearRegression
model = SimpleLinearRegression()


# %%NBQA-CELL-SEPfaab7c
# применим метод .fit()
model.fit(X, y)

# посмотрим на коэффициенты
model.slope_, model.intercept_


# %%NBQA-CELL-SEPfaab7c
# сделаем прогноз через .predict()
y_pred = model.predict(X)

# и выведем первые пять коэффициентов
y_pred[:5]
