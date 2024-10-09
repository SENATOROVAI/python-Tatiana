# %%NBQA-CELL-SEPfaab7c
"Module on class functions and methods of instances.Binding."


# %%NBQA-CELL-SEPfaab7c
class Person:
    # function prints hello
    def hello():
        print("hello")


# %%NBQA-CELL-SEPfaab7c
# Look at the function as an object of the class
Person.hello


# %%NBQA-CELL-SEPfaab7c
object = Person()
object.hello
# pointing at the instanse of class Person:
# <__main__.Person object at 0x7feca07c5510


# %%NBQA-CELL-SEPfaab7c
print(id(object))  # id ofoject of class Person
print(hex(id(object)))  # id in hex format


# %%NBQA-CELL-SEPfaab7c
print(Person.hello())


# %%NBQA-CELL-SEPfaab7c
print(type(Person.hello))


# %%NBQA-CELL-SEPfaab7c
object.hello()


# %%NBQA-CELL-SEPfaab7c
print(type(object.hello))


# %%NBQA-CELL-SEPfaab7c
# id of the function object
print(id(Person.hello))


# %%NBQA-CELL-SEPfaab7c
# id of the instance object
print(id(object.hello))


# %%NBQA-CELL-SEPfaab7c
#  id of the function object
# id of the instance object

dir(Person.hello) == dir(object.hello)


# %%NBQA-CELL-SEPfaab7c
object.hello.__self__


# %%NBQA-CELL-SEPfaab7c
hex(id(object))


# %%NBQA-CELL-SEPfaab7c
object.hello.__func__


# %%NBQA-CELL-SEPfaab7c
class Person:
    def hello(instance):
        print(instance)


# %%NBQA-CELL-SEPfaab7c
inst = Person()
inst.hello()


# %%NBQA-CELL-SEPfaab7c
hex(id(inst))


# %%NBQA-CELL-SEPfaab7c
class Person:
    def hello(self):
        print(self)


# %%NBQA-CELL-SEPfaab7c
inst = Person()
inst.hello()
