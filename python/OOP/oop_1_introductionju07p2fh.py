# %%NBQA-CELL-SEPfaab7c
"Module on oop"


# %%NBQA-CELL-SEPfaab7c
class Person:
    name = "Ivan"


# %%NBQA-CELL-SEPfaab7c
# to get an attribute of class Person -
# use DOT NOTATION.
Person.name


# %%NBQA-CELL-SEPfaab7c
# to know the name of the class
# use __name__ - dunder method
Person.__name__


# %%NBQA-CELL-SEPfaab7c
# to see all availabele attributes
dir("Person")


# %%NBQA-CELL-SEPfaab7c
Person.__class__


# %%NBQA-CELL-SEPfaab7c
# call the class = create an object of the class
object = Person()


# %%NBQA-CELL-SEPfaab7c
object.__class__
# link to module.class name


# %%NBQA-CELL-SEPfaab7c
# returns a string
object.__class__.__name__


# %%NBQA-CELL-SEPfaab7c
# returns class as an object
type(object)


# %%NBQA-CELL-SEPfaab7c
new_person = type(object)()  # call type(object)
new_person


# %%NBQA-CELL-SEPfaab7c
# compare ids of two objects
print(id(new_person) == id(object))
