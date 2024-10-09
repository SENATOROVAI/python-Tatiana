# %%NBQA-CELL-SEPfaab7c
# создадим класс CatClass
class CatClass:

    # и пропишем метод .__init__()
    def __init__(self):
        pass


# %%NBQA-CELL-SEPfaab7c
# создадим объект Matroskin класса CatClass
Matroskin = CatClass()

# проверим тип данных созданной переменной
type(Matroskin)


# %%NBQA-CELL-SEPfaab7c
# вновь создадим класс CatClass
class CatClass:

    # метод .__init__() на этот раз принимает еще и параметр color
    def __init__(self, color):

        # этот параметр будет записан в переменную атрибута self.color
        self.color = color

        # значение атрибута type_ задается внутри класса
        self.type_ = "cat"


# %%NBQA-CELL-SEPfaab7c
# повторно создадим объект класса CatClass, передав ему параметр цвета шерсти
Matroskin = CatClass("gray")

# и выведем атрибуты класса
Matroskin.color, Matroskin.type_


# %%NBQA-CELL-SEPfaab7c
# перепишем класс CatClass
class CatClass:

    # метод .__init__() и атрибуты оставим без изменений
    def __init__(self, color):
        self.color = color
        self.type_ = "cat"

    # однако добавим метод, который позволит коту мяукать
    def meow(self):
        for i in range(3):
            print("Мяу")

    # и метод .info() для вывода информации об объекте
    def info(self):
        print(self.color, self.type_)


# %%NBQA-CELL-SEPfaab7c
# создадим объект
Matroskin = CatClass("gray")


# %%NBQA-CELL-SEPfaab7c
# применим метод .meow()
Matroskin.meow()


# %%NBQA-CELL-SEPfaab7c
# и метод .info()
Matroskin.info()


# %%NBQA-CELL-SEPfaab7c
# изменим атрибут type_ объекта Matroskin на dog
Matroskin.type_ = "dog"

# выведем этот атрибут
Matroskin.type_


# %%NBQA-CELL-SEPfaab7c
class CatClass:

    def __init__(self, color):
        self.color = color
        # символ подчеркивания ПЕРЕД названием атрибута указывает,
        # что это частный атрибут и изменять его не стоит
        self._type_ = "cat"


# %%NBQA-CELL-SEPfaab7c
# вновь создадим объект класса CatClass
Matroskin = CatClass("gray")

# и изменим значение атрибута _type_
Matroskin._type_ = "dog"
Matroskin._type_


# %%NBQA-CELL-SEPfaab7c
class CatClass:

    def __init__(self, color):
        self.color = color
        # символ двойного подчеркивания предотвратит доступ извне
        self.__type_ = "cat"


# %%NBQA-CELL-SEPfaab7c
# при попытке вызова такого атрибута Питон выдаст ошибку
Matroskin = CatClass("gray")
# Matroskin.__type_


# %%NBQA-CELL-SEPfaab7c
# поставим _CatClass перед __type_
Matroskin._CatClass__type_ = "dog"

# к сожалению, значение атрибута изменится
Matroskin._CatClass__type_


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
pigeon = Bird(0.3, 30)


# %%NBQA-CELL-SEPfaab7c
# посмотрим на унаследованные у класса Animal атрибуты
pigeon.weight, pigeon.length


# %%NBQA-CELL-SEPfaab7c
# и методы
pigeon.eat()


# %%NBQA-CELL-SEPfaab7c
# теперь вызовем метод, свойственный только классу Bird
pigeon.move()


# %%NBQA-CELL-SEPfaab7c
# снова создадим класс Bird
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
pigeon.weight, pigeon.length, pigeon.flying_speed


# %%NBQA-CELL-SEPfaab7c
# вызовем унаследованный метод .sleep()
pigeon.sleep()


# %%NBQA-CELL-SEPfaab7c
# и собственный метод .move()
pigeon.move()


# %%NBQA-CELL-SEPfaab7c
# создадим подкласс Flightless класса Bird
class Flightless(Bird):

    # метод .__init__() этого подкласса "стирает" .__init__() родительского класса
    def __init__(self, running_speed):

        # таким образом, у нас остается только один атрибут
        self.running_speed = running_speed

    # кроме того, результатом метода .move() будет 'Running'
    def move(self):
        print("Running")


# %%NBQA-CELL-SEPfaab7c
# создадим объект ostrich класса Flightless
ostrich = Flightless(60)


# %%NBQA-CELL-SEPfaab7c
# посмотрим на значение атрбута скорости
ostrich.running_speed


# %%NBQA-CELL-SEPfaab7c
# и проверим метод .move()
ostrich.move()


# %%NBQA-CELL-SEPfaab7c
# подкласс Flightless сохранил методы всех родительских классов
ostrich.eat()


# %%NBQA-CELL-SEPfaab7c
# создадим родительский класс Fish
class Fish:

    # и метод .swim()
    def swim(self):
        print("Swimming")


# %%NBQA-CELL-SEPfaab7c
# и еще один родительский класс Bird
class Bird:

    # и метод .fly()
    def fly(self):
        print("Flying")


# %%NBQA-CELL-SEPfaab7c
# теперь создадим класс-потомок этих двух классов
class SwimmingBird(Bird, Fish):
    pass


# %%NBQA-CELL-SEPfaab7c
# создадим объект duck класса SwimmingBird
duck = SwimmingBird()


# %%NBQA-CELL-SEPfaab7c
# как мы видим утка умеет как летать,
duck.fly()


# %%NBQA-CELL-SEPfaab7c
# так и плавать
duck.swim()


# %%NBQA-CELL-SEPfaab7c
# для чисел '+' является оператором сложения
2 + 2


# %%NBQA-CELL-SEPfaab7c
# для строк - оператором объединения
"классы" + " и " + "объекты"


# %%NBQA-CELL-SEPfaab7c
# функцию len() можно применить к строке
len("Программирование на Питоне")


# %%NBQA-CELL-SEPfaab7c
# кроме того, она способна работать со списком
len(["Программирование", "на", "Питоне"])


# %%NBQA-CELL-SEPfaab7c
# словарем
len({0: "Программирование", 1: "на", 2: "Питоне"})


# %%NBQA-CELL-SEPfaab7c
# массивом Numpy и другими объектами
import numpy as np

len(np.array([1, 2, 3]))


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
# создадим класс собак
class DogClass:

    # с такими же атрибутами
    def __init__(self, name, color):
        self.name = name
        self._type_ = "пес"
        self.color = color

    # и методами
    def info(self):
        print(f"Меня зовут {self.name}, я {self._type_}, цвет моей шерсти {self.color}")

    # хотя, обратите внимание, действия внутри методов отличаются
    def sound(self):
        print("Я умею лаять")


# %%NBQA-CELL-SEPfaab7c
cat = CatClass("Бегемот", "черный")
dog = DogClass("Барбос", "серый")


# %%NBQA-CELL-SEPfaab7c
for animal in (cat, dog):
    animal.info()
    animal.sound()
    print()


# %%NBQA-CELL-SEPfaab7c
patients = [
    {"name": "Николай", "height": 178},
    {"name": "Иван", "height": 182},
    {"name": "Алексей", "height": 190},
]


# %%NBQA-CELL-SEPfaab7c
# создадим переменные для общего роста и количества пациентов
total, count = 0, 0

# в цикле for пройдемся по пациентам (отдельным словарям)
for patient in patients:
    # достанем значение роста и прибавим к текущему значению переменной total
    total += patient["height"]
    # на каждой итерации будем увеличивать счетчик пациентов на один
    count += 1

# разделим общий рост на количество пациентов,
# чтобы получить среднее значение
total / count


# %%NBQA-CELL-SEPfaab7c
patients = [
    {"name": "Николай", "height": 178},
    {"name": "Иван", "height": 182},
    {"name": "Алексей", "height": 190},
]


# %%NBQA-CELL-SEPfaab7c
# создадим класс для работы с данными DataClass
class DataClass:

    # при создании объекта будем передавать ему данные для анализа
    def __init__(self, data):
        self.data = data

    # кроме того, создадим метод для расчета среднего значения
    def count_average(self, metric):

        # параметр metric определит, по какому столбцу считать среднее
        self.metric = metric

        # объявим два частных атрибута
        self.__total = 0
        self.__count = 0

        # в цикле for пройдемся по списку словарей
        for item in self.data:

            # рассчитем общую сумму по указанному в metric
            # значению каждого словаря
            self.__total += item[self.metric]

            # и количество таких записей
            self.__count += 1

        # разделим общую сумму показателя на количество записей
        return self.__total / self.__count


# %%NBQA-CELL-SEPfaab7c
# создадим объект класса DataClass и передадим ему данные о пациентах
data_object = DataClass(patients)

# вызовем метод .count_average() с метрикой 'height'
data_object.count_average("height")


# %%NBQA-CELL-SEPfaab7c
# lambda-функция достанет значение по ключу height
# функция map() применит lambda-функцию к каждому вложенному в patients словарю
# функция list() преобразует результат в список
heights = list(map(lambda x: x["height"], patients))
heights


# %%NBQA-CELL-SEPfaab7c
# воспользуемся функциями sum() и len() для нахождения среднего значения
sum(heights) / len(heights)


# %%NBQA-CELL-SEPfaab7c
# возьмем два двумерных массива
a = np.array([[0, 1, 2], [3, 4, 5]])

b = np.array([[5, 4], [3, 2], [1, 0]])


# %%NBQA-CELL-SEPfaab7c
# перемножим a и b по индексу j через функцию np.einsum()
np.einsum("ij, jk -> ik", a, b)


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
# преобразуем данные роста в двумерный массив
X_2D = X.reshape(-1, 1)


# %%NBQA-CELL-SEPfaab7c
# из набора линейных моделей библиотеки sklearn импортируем линейную регрессию
from sklearn.linear_model import LinearRegression

# создадим объект этого класса и запишем в переменную model
model = LinearRegression()

# обучим модель с помощью метода .fit(), которому передадим наши данные
model.fit(X_2D, y)

# на выходе получим коэффициенты линейной регрессии
model.coef_, model.intercept_


# %%NBQA-CELL-SEPfaab7c
# построим прогноз и выведем первые пять значений
y_pred = model.predict(X_2D)
y_pred[:5]


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
