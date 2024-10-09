# %%NBQA-CELL-SEPfaab7c
import itertools
from itertools import combinations, combinations_with_replacement, permutations


# %%NBQA-CELL-SEPfaab7c
# 0!,1! = 1#


def factorial(num: int) -> int:  # -> указать тип который возращает функция
    """Интерпретатор возвращаеттип данных none"""
    if num == 0 or num == 1:
        # num = num*(num-1)
        return 1

    # print(num)# Возвращает NOne

    return num * factorial(
        num - 1
    )  # используется когда надо передать значение из функции дальше


# print(factorial(1))#

get_num = factorial(5)  #

print(get_num)


# %%NBQA-CELL-SEPfaab7c
# скольктми способами можно переставить яблоко банан и грушу
# Перестановка без повторениий
# P3! = 3!=3*2*1


def fac(num):
    if num == 0:
        return 1
    return num * fac(num - 1)


print(fac(3))


# %%NBQA-CELL-SEPfaab7c
fruits = ["banana", "apple", "pear"]
permutations_ = permutations(fruits)
# print(dir(permutations_))
# print(permutations_.__next__())
# print(permutations_.__next__())
len(list(permutations_))

for item in combinations(fruits, 2):
    print(item)


# %%NBQA-CELL-SEPfaab7c
# how many ways can I rearrange the letters in a word
wrd_1 = "МАЙ"
wrd_2 = "ИЮНЬ"
wrd_3 = "ОСЕНЬ"

# Permutations(перестановки)
# 1) 3! = 6
# 2) 4! = 24
# 3) 5! = 12


# %%NBQA-CELL-SEPfaab7c
# Decision using def fac
print(fac(len(wrd_1)))  #
print(fac(len(wrd_2)))  #
print(fac(len(wrd_3)))  #


# %%NBQA-CELL-SEPfaab7c
# Decision using itertools

var_1 = permutations(wrd_1, r=None)
var_2 = permutations(wrd_2, r=None)
var_3 = permutations(wrd_3, r=None)
len(list(var_1)), len(list(var_2)), len(list(var_3))


# %%NBQA-CELL-SEPfaab7c
# how many ways can I rearrange letters in words
# a)how many three-digit numbers can be made up of digits
# lst_1 = [1, 2, 3, 4, 5]
lst_1 = [0, 1, 2, 3, 4]
# number of placements

# b) how many three-digit numbers consisting of different digits can be composed from the digits
lst_2 = [1, 2, 3, 4]


# %%NBQA-CELL-SEPfaab7c
digits3_1: list = list(permutations(lst_1, r=3))
digits3_2: list = list(combinations(lst_2, r=2))
print(digits3_1, digits3_2, sep="\n")


# %%NBQA-CELL-SEPfaab7c
print(f"digits3_1 number of permutations of  - {len(digits3_1)} ")
print(f"digits3_2 number of combinations of  - {len(digits3_2)} ")


# %%NBQA-CELL-SEPfaab7c
# Var1
# Write down all possible combinations and all possible placements of 4 elements of a set of 3 elements.
lst_3 = list("abcd")
string_comb = list(combinations(lst_3, 3))
string_perm = list(permutations(lst_3, 3))
print(f" Number of combinations 'abcd': {len(string_comb)}")
print(f" Number of combinations 'abcd': {len(string_perm)}")


# %%NBQA-CELL-SEPfaab7c
print(lst_3)


# %%NBQA-CELL-SEPfaab7c
# Var 2
# combinations
# C3_4 = 4!/(4-3)!*3! = (3!*4)/3! = 4
lst_3 = [i for i in "abcd"]  # ['a', 'b', 'c', 'd']

comb = list(combinations(lst_3, 3))
count_comb = 0
for i in lst_3:
    count_comb += 1

print(comb)
print(count_comb)


# %%NBQA-CELL-SEPfaab7c
# A3_4 = 4!/(4-3)! = 4! = 4*3*2=24

lst_3 = [i for i in "abcd"]  # ['a', 'b', 'c', 'd']

perm = list(permutations(lst_3, 3))

count_perm = 0
for i in perm:
    count_perm += 1
# print(perm)
print(count_perm)


# %%NBQA-CELL-SEPfaab7c
# how many ways are there to distribute 3 awards among 10 competitors?
competitors = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
AWARDS = 3

# if the awards are equal => comninations.C3_10 = 10!/(7!*3!) = (8*9*10)/6 = 120

awards_comb = combinations(competitors, AWARDS)
print(
    f" Number of combinationd to divide 3 equal awards among 10 competitors -  {len(list(awards_comb))}"
)

# if the awards are different => permutatios.C3_10 = 10!/3! = 4*5*6*7*8*9*10 =

awards_perm = permutations(competitors, AWARDS)
print(
    f" Number of permutations to divide 3 different awards among 10 competitors -  {len(list(awards_perm))}"
)


# %%NBQA-CELL-SEPfaab7c
# a)how many ways are there to choose 3 flowers from a vase containing 6 roses and 5 carnations?
count_flow = list(range(1, 12))  # 6 + 5
var_6 = itertools.permutations(count_flow, 3)
# b)how many ways are there to choose 1 rose and 2 carnations from this vase?
var_m = itertools.permutations(list(range(1, 7)), 1)
var_n = itertools.permutations(list(range(1, 6)), 2)
len(list(var_6)), len(list(var_m)) + len(list(var_n))


# %%NBQA-CELL-SEPfaab7c
# Combination with repeated elements
# C3_2(rep) = C3_(3+2-1) = C3_4 = 4!/(4-1)!*3!=3!*4/3!=4

combinations = list(combinations_with_replacement(["rose", "carnation"], 3))

print(len(combinations))


# %%NBQA-CELL-SEPfaab7c
abc = ("a", "b", "c")

print([(var_x, var_y, var_z) for var_x in abc for var_y in abc for var_z in abc])
