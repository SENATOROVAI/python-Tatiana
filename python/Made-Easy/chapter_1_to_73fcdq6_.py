# %%NBQA-CELL-SEPfaab7c
"Module intoduction to python."


# %%NBQA-CELL-SEPfaab7c
from sympy import isprime


# %%NBQA-CELL-SEPfaab7c
ls = []  #
simple = [1, 2]
for i in range(3, 101):
    for num in ls:
        if i % num != 0:
            simple.append(j)
print(simple)


# %%NBQA-CELL-SEPfaab7c
print(isprime(5))


# %%NBQA-CELL-SEPfaab7c
num = 1
total_sum = 0
while num != 101:
    if num % 2 == 0:
        total_sum += num
    num += 1
print(total_sum)


# %%NBQA-CELL-SEPfaab7c
ls = []
for i in range(1, 16, 2):
    ls.append(i**2)

print(ls)


# %%NBQA-CELL-SEPfaab7c
for i in range(1, 11):
    print(f"{i} * 3 = {i*3}")


# %%NBQA-CELL-SEPfaab7c
entrance_amount = int(input())
percentage = int(input())
period = int(input())
final_amount = entrance_amount * (1 + percentage / 100) ** period
print(final_amount)
