# %%NBQA-CELL-SEPfaab7c
kirk = ["James Kirk", 34, "Captain", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]


# %%NBQA-CELL-SEPfaab7c
class Dog:
    pass


# %%NBQA-CELL-SEPfaab7c
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# %%NBQA-CELL-SEPfaab7c
class Dog:
    # Атрибут класса
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age


# %%NBQA-CELL-SEPfaab7c
class Dog:
    pass


# %%NBQA-CELL-SEPfaab7c
Dog()


# %%NBQA-CELL-SEPfaab7c
Dog()


# %%NBQA-CELL-SEPfaab7c
a = Dog()
b = Dog()
a == b


# %%NBQA-CELL-SEPfaab7c
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age


# %%NBQA-CELL-SEPfaab7c
Dog()


# %%NBQA-CELL-SEPfaab7c
buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)


# %%NBQA-CELL-SEPfaab7c
buddy.name


# %%NBQA-CELL-SEPfaab7c
buddy.age


# %%NBQA-CELL-SEPfaab7c
miles.name


# %%NBQA-CELL-SEPfaab7c
miles.age


# %%NBQA-CELL-SEPfaab7c
buddy.species


# %%NBQA-CELL-SEPfaab7c
miles.species


# %%NBQA-CELL-SEPfaab7c
buddy.age = 10
buddy.age


# %%NBQA-CELL-SEPfaab7c
miles.species = "Felis silvestris"
miles.species


# %%NBQA-CELL-SEPfaab7c
buddy.species


# %%NBQA-CELL-SEPfaab7c
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Метод экземпляра
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Другой метод экземпляра
    def speak(self, sound):
        return f"{self.name} says {sound}"


# %%NBQA-CELL-SEPfaab7c
miles = Dog("Miles", 4)
miles.description()


# %%NBQA-CELL-SEPfaab7c
miles.speak("Woof Woof")


# %%NBQA-CELL-SEPfaab7c
miles.speak("Bow Wow")


# %%NBQA-CELL-SEPfaab7c
names = ["Fletcher", "David", "Dan"]
print(names)


# %%NBQA-CELL-SEPfaab7c
print(miles)


# %%NBQA-CELL-SEPfaab7c
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


# %%NBQA-CELL-SEPfaab7c
miles = Dog("Miles", 4)
print(miles)


# %%NBQA-CELL-SEPfaab7c
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


# %%NBQA-CELL-SEPfaab7c
miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")


# %%NBQA-CELL-SEPfaab7c
buddy.speak("Yap")


# %%NBQA-CELL-SEPfaab7c
jim.speak("Woof")


# %%NBQA-CELL-SEPfaab7c
jack.speak("Woof")


# %%NBQA-CELL-SEPfaab7c
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


# %%NBQA-CELL-SEPfaab7c
class JackRussellTerrier(Dog):
    pass


class Dachshund(Dog):
    pass


class Bulldog(Dog):
    pass


# %%NBQA-CELL-SEPfaab7c
miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)


# %%NBQA-CELL-SEPfaab7c
miles.species


# %%NBQA-CELL-SEPfaab7c
buddy.name


# %%NBQA-CELL-SEPfaab7c
print(jack)


# %%NBQA-CELL-SEPfaab7c
jim.speak("Woof")


# %%NBQA-CELL-SEPfaab7c
type(miles)


# %%NBQA-CELL-SEPfaab7c
isinstance(miles, Dog)


# %%NBQA-CELL-SEPfaab7c
isinstance(miles, Bulldog)


# %%NBQA-CELL-SEPfaab7c
isinstance(jack, Dachshund)


# %%NBQA-CELL-SEPfaab7c
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"


# %%NBQA-CELL-SEPfaab7c
miles = JackRussellTerrier("Miles", 4)
miles.speak()


# %%NBQA-CELL-SEPfaab7c
miles.speak("Grrr")


# %%NBQA-CELL-SEPfaab7c
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} barks {sound}"


# %%NBQA-CELL-SEPfaab7c
miles = JackRussellTerrier("Miles", 4)
miles.speak()


# %%NBQA-CELL-SEPfaab7c
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)


# %%NBQA-CELL-SEPfaab7c
miles = JackRussellTerrier("Miles", 4)
miles.speak()
