# %%NBQA-CELL-SEPfaab7c
"Module on class instances."


# %%NBQA-CELL-SEPfaab7c
class Person:
    name = "Ivan"

    def hello():
        print("Hello")


# %%NBQA-CELL-SEPfaab7c
# create an instance of class Person()
per_1 = Person()
print(per_1)


# %%NBQA-CELL-SEPfaab7c
# create another instance of class Person()
per_2 = Person()
print(per_2)


# %%NBQA-CELL-SEPfaab7c
# these instances are different as id differs
id(per_1) == id(per_2)


# %%NBQA-CELL-SEPfaab7c
# attributes are the same for per_1 and per_2
print(per_1.name, per_2.name)


# %%NBQA-CELL-SEPfaab7c
# ids of attribues are equal and determined in the class
print(id(per_1.name), id(per_2.name), id(Person.name))


# %%NBQA-CELL-SEPfaab7c
# local namespace
per_1.__dict__, per_2.__dict__


# %%NBQA-CELL-SEPfaab7c
Person.__dict__


# %%NBQA-CELL-SEPfaab7c
# assign new meanings to existing attributes

per_1.name = "Oleg"
per_2.name = "Olga"


# %%NBQA-CELL-SEPfaab7c
per_1.__dict__, per_2.__dict__


# %%NBQA-CELL-SEPfaab7c
# create a new attribure to the instance
per_2.age = 22


# %%NBQA-CELL-SEPfaab7c
per_2.__dict__
