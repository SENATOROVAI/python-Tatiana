# %%NBQA-CELL-SEPfaab7c
"Module on class functions."


# %%NBQA-CELL-SEPfaab7c
class Person:
    name = "Ivan"  # atribute = field = property


# %%NBQA-CELL-SEPfaab7c
# check out with dir()
dir(Person)


# %%NBQA-CELL-SEPfaab7c
Person.__dict__


# %%NBQA-CELL-SEPfaab7c
Person.name


# %%NBQA-CELL-SEPfaab7c
Person.age = 12121


# %%NBQA-CELL-SEPfaab7c
Person.__dict__


# %%NBQA-CELL-SEPfaab7c
getattr(Person, "name")


# %%NBQA-CELL-SEPfaab7c
# set a new attribute
# (class name, "attribute name", meaning)
setattr(Person, "date_birth", 1987)


# %%NBQA-CELL-SEPfaab7c
Person.__dict__


# %%NBQA-CELL-SEPfaab7c
# change the meaning of the existing attribute
setattr(Person, "name", "Lena")


# %%NBQA-CELL-SEPfaab7c
Person.__dict__


# %%NBQA-CELL-SEPfaab7c
# delete the attribute

delattr(Person, "date_birth")


# %%NBQA-CELL-SEPfaab7c
Person.__dict__


# %%NBQA-CELL-SEPfaab7c
class Person:
    name = "Ivan"
    # name the function - def name():

    def hello():
        print("Hello")


# call the hello function:
Person.hello()


# %%NBQA-CELL-SEPfaab7c
print(Person.__dict__)
