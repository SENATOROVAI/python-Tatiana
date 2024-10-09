# %%NBQA-CELL-SEPfaab7c
hash(0xF9449A7D)


# %%NBQA-CELL-SEPfaab7c
a = 121
print(bin(a))  # presenting a in bits
~a  # formulae: (-1) * 121-1 = -122


# %%NBQA-CELL-SEPfaab7c
d = 0
print(~d, "for 0")
c = 11
print(~c, "for 11")
h = -8
print(~h, "for -8")


# %%NBQA-CELL-SEPfaab7c
flags = 5
mask = 4
res = flags & mask  # & побитовое умножение = конъюнкция
# flags &= mask # short form
print("5:", bin(flags))
print("4:", bin(mask))
print("res:", bin(res))
res


# %%NBQA-CELL-SEPfaab7c
flags = 5  # 1
mask = 4
if flags & mask == mask:  # we check whether the 2d bin in num 5 is on or not
    print("2d bin is on")
else:
    print("2d bin is off")


# %%NBQA-CELL-SEPfaab7c
flags = 13  #
mask = 5
flags_res = flags & ~mask  # we check whether the 2d bin in num 5 is on or not
print("1) flags 13:", bin(flags))  # does not change
print()
print("2) mask to ~mask ( 5=>-6):", bin(mask), bin(~mask))

print("flags_res:", bin(flags_res))
print(flags_res)


# %%NBQA-CELL-SEPfaab7c
flags = 8  #
mask = 5
# flags_res = flags | mask # we check whether the 2d bin in num 5 is on or not
flags_res |= mask  # short form
print(f"1) flags {flags}:", bin(flags))  # does not change

print(f"2) mask {mask}:", bin(mask))

print(f"3) flags_res {flags_res}:", bin(flags_res))


# %%NBQA-CELL-SEPfaab7c
x ^= y  # =>                      (x ^ y, y)
y ^= x  # => (x ^ y, y ^ x ^ y) = (x ^ y, x)
x ^= y  # => (x ^ y ^ x, x)     = (y, x)


# %%NBQA-CELL-SEPfaab7c
flags = 9  # x1
mask = 1  # x2 switching off the 1st bin
flags_res = flags ^ mask  # we check whether the 2d bin in num 5 is on or not
# flags_res = flags ^ mask # если применить xor дважды к одной переменной то выйдем на эту же переименную.Тк  биты у нас переключились обратно.
#  flags ^= mask # short form
print(f"1) flags {flags}:", bin(flags))  # does not change

print(f"2) mask {mask}:", bin(mask))

print(f"3) flags_res {flags_res}:", bin(flags_res))


# %%NBQA-CELL-SEPfaab7c
x = 160
print(f"{x}", bin(x))
x = x >> 1  # сдвигаем биты вправо на 1 = devide an origin by 2
print(f"{x}", bin(x))  # стало на 1 ноль меньше

x = x >> 2  # сдвигаем биты вправо на 2 = devide an origin by 2**2
print(f"{x}", bin(x))

x = x >> 2  # сдвигаем биты вправо на 2 = devide an origin by 2**2
print(f"{x}", bin(x))

x = x >> 1  # сдвигаем биты вправо на 1 = devide an origin by 2
print(f"{x}", bin(x))
# x >> 1 == x//2
# x >> 2 == x//4


# %%NBQA-CELL-SEPfaab7c
x = 2
print(f"{x}", bin(x))
x = x << 1  # сдвигаем биты влево на 1 = multiply an origin by 2
print(f"{x}", bin(x))  #
x = x << 3  # multiply an origin by 2**3
print(f"{x}", bin(x))  #
