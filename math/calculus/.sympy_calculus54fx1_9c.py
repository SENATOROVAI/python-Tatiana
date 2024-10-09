# %%NBQA-CELL-SEPfaab7c
import sympy as sp


# %%NBQA-CELL-SEPfaab7c
sp.cbrt(x - 6)  # root 3 from (x-6)


# %%NBQA-CELL-SEPfaab7c
# log
sp.log(16, 2)  # log(result, base)


# %%NBQA-CELL-SEPfaab7c
x = sp.symbols("x")
expr = x + 1  # function
expr.subs(x, 2)


# %%NBQA-CELL-SEPfaab7c
n = sp.symbols("n")
s = n * (n + 1) * (2 * n + 1) / 6  # formulae for sum of sqaures
limit = sp.limit(s / n**3, n, sp.oo)
limit


# %%NBQA-CELL-SEPfaab7c
x = sp.symbols("x")
f = (sp.sqrt(4 + x) - 2) / (3 * sp.atan(x))

limit = sp.limit(f, x, 0)
limit
f


# %%NBQA-CELL-SEPfaab7c
x = sp.symbols("x")
f = ((x + 3) / (x - 2)) ** (2 * x + 1)
limit = sp.limit(f, x, sp.oo)  # sp.oo  - infinity
limit


# %%NBQA-CELL-SEPfaab7c
x = sp.symbols("x")
f = (1 - sp.ln(1 + x**3)) ** (3 / (x**2 * sp.asin(x)))
limit = sp.limit(f, x, 0)
limit


# %%NBQA-CELL-SEPfaab7c
# 1
n = sp.symbols("n")  # crate symbol n
f = (n * ((7 * n) ** (1 / 3)) - (81 * (n**8) - 1) ** (1 / 4)) / (
    (n + 4 * n ** (1 / 2)) * ((n**2 - 5) ** (1 / 2))
)  # ctreate a function
lim = sp.limit(f, n, sp.oo)
lim


# %%NBQA-CELL-SEPfaab7c
# 2

n = sp.symbols("n")

f = (3**n - 2**n) / (3**n - 1 + 2**n)
limit = sp.limit(f, n, sp.oo)
limit


# %%NBQA-CELL-SEPfaab7c
# 3

x = sp.symbols("x")

f = (2 * x**2 - 9 * x + 10) / (2 * x - 5)
limit = sp.limit(f, x, 5 / 2)
limit


# %%NBQA-CELL-SEPfaab7c
# 4
x = sp.symbols("x")

f = (sp.cbrt(x - 6) + 2) / (x + 2)
# f = (sp.cbrt((x-6),3)+2)/(x+2) # 2d varient
limit = sp.limit(f, x, -2)
limit
# f


# %%NBQA-CELL-SEPfaab7c
# 1

x = sp.symbols("x")

f = ((4 + x) ** (1 / 2) - 2) / (3 * sp.atan(x))
limit = sp.limit(f, x, 0)
limit


# %%NBQA-CELL-SEPfaab7c
# 2

x = sp.symbols("x")

f = (2**x - 16) / (sp.sin(sp.pi * x))
limit = sp.limit(f, x, 4)
limit


# %%NBQA-CELL-SEPfaab7c
# 3
x = sp.symbols("x")

f = (sp.cos(x / 2)) / (sp.E ** (sp.sin(x)) - sp.E ** (sp.sin(4 * x)))
limit = sp.limit(f, x, sp.pi)
limit


# %%NBQA-CELL-SEPfaab7c
# 4

x = sp.symbols("x")

f = (sp.E ** (2 * x) - sp.E ** (x)) / (sp.sin(3 * x) - sp.sin(5 * x))
limit = sp.limit(f, x, 0)
limit


# %%NBQA-CELL-SEPfaab7c
# 5

x = sp.symbols("x")

f = (1 - x) / sp.log(x, 2)
limit = sp.limit(f, x, 1)
limit


# %%NBQA-CELL-SEPfaab7c
# 6

x = sp.symbols("x")

f = sp.cos(x) ** (1 / (sp.ln(1 + sp.sin(x) ** 2)))
limit = sp.limit(f, x, 0)
limit


# %%NBQA-CELL-SEPfaab7c
# 7
x = sp.symbols("x")

f = sp.sin(x + 2) ** (3 / (3 + x))
limit = sp.limit(f, x, 0)
limit


# %%NBQA-CELL-SEPfaab7c
# 8

x = sp.symbols("x")

f = sp.sin(x) ** (6 * sp.tan(x) * sp.tan(3 * x))
limit = sp.limit(f, x, sp.pi / 2)
limit


# %%NBQA-CELL-SEPfaab7c
# 9
x = sp.symbols("x")

f = (((x + 2) ** (1 / 2) - 2) / (x**2 - 4)) ** (1 / x)
limit = sp.limit(f, x, 2)
limit


# %%NBQA-CELL-SEPfaab7c
# 10

x = sp.symbols("x")

f = ((sp.tan(x)) ** (1 / 3) * sp.atan(1 / x) + 3) / (2 - sp.tan(1 + sp.sin(x)))
limit = sp.limit(f, x, 0)
limit
f


# %%NBQA-CELL-SEPfaab7c
x = sp.symbols("x")

f = (sp.cbrt(x**2) * sp.sin(x**2)) / (x - 1)
limit = sp.limit(f, x, sp.oo)
limit
# f


# %%NBQA-CELL-SEPfaab7c
x = sp.symbols("x")

f = sp.cbrt(x)
limit = sp.limit(f, x, sp.oo)
limit
# f


# %%NBQA-CELL-SEPfaab7c
x = sp.symbols("x")

f = sp.sqrt(x + 2) - sp.sqrt(x)
limit = sp.limit(f, x, sp.oo)
limit
# f
