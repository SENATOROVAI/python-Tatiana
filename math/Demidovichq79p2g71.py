# %%NBQA-CELL-SEPfaab7c
"""Modele on solving problems in Demidovich."""


# %%NBQA-CELL-SEPfaab7c
import matplotlib.pyplot as plt
import numpy as np

hash(0x79D14938)


# %%NBQA-CELL-SEPfaab7c
var_a = np.array([2, 7], dtype="int8")  # vector array
var_b = np.zeros(2, dtype="int8")  # creating a zero vector, size()


# %%NBQA-CELL-SEPfaab7c
print(var_a.shape, var_b.shape)
""" As we can see the sizes of vectors var_a and var_b are equal.
 Thus we can add one vector to another """


# %%NBQA-CELL-SEPfaab7c
var_c = var_a + var_b
print(var_c, var_c.dtype)


# %%NBQA-CELL-SEPfaab7c
# we create 2 vectors of equal size and then check the commutativity property
var_a1 = np.array([4, 5, 8])
var_a2 = np.array([8, 4, 1])


# %%NBQA-CELL-SEPfaab7c
if np.any(var_a1 + var_a2 == var_a2 + var_a1):
    print(
        f"The commutativity property has been proven:a1+a2 = a2+a1{var_a1+var_a2 == var_a2+var_a1} "
    )
else:
    print("The commutativity's failed")


# %%NBQA-CELL-SEPfaab7c
# Create a single vector
var_v = np.array([1, 1])
var_v2 = np.array([1, -1])
var_v3 = np.array([-2, 0])

var_v4 = np.array([1, -1])
var_v5 = np.array([1, 1])
var_v6 = np.array([2, 0])
# Create the plot
fig, ax = plt.subplots()

# Add the vector V to the plot
ax.quiver(0, 0, var_v[0], var_v[1], angles="xy", scale_units="xy", scale=1, color="r")
ax.quiver(
    -1, 1, var_v2[0], var_v2[1], angles="xy", scale_units="xy", scale=1, color="g"
)
ax.quiver(1, 1, var_v3[0], var_v3[1], angles="xy", scale_units="xy", scale=1, color="b")

ax.quiver(0, 2, var_v4[0], var_v4[1], angles="xy", scale_units="xy", scale=1, color="g")
ax.quiver(
    -1, 1, var_v5[0], var_v5[1], angles="xy", scale_units="xy", scale=1, color="r"
)
ax.quiver(
    -1, 1, var_v6[0], var_v6[1], angles="xy", scale_units="xy", scale=1, color="y"
)
# Set the x-limits and y-limits of the plot
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])

# Show the plot along with the grid
plt.grid()
plt.show()

print(len(var_v) == len(var_v5))
print(len(var_v2) == len(var_v4))
print(len(var_v3) == len(var_v6))


# %%NBQA-CELL-SEPfaab7c
var_x = [0, -1, 1, 0, -1, -1]
var_y = [0, 1, 1, 2, 1, 1]
var_u = [1, 1, -2, 1, 1, 2]
var_v = [1, -1, 0, -1, 1, 0]
plt.quiver(
    var_x,
    var_y,
    var_u,
    var_v,
    angles="xy",
    scale_units="xy",
    scale=1,
    color=["r", "g", "b", "g", "r", "y"],
)
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.grid()
plt.show()


# %%NBQA-CELL-SEPfaab7c
var_x = [0, -1, 1, 0, -1, -1]
var_y = [0, 1, 1, 2, 1, 1]
var_u = [1, 1, -2, 1, 1, 2]
var_v = [1, -1, 0, -1, 1, 0]
plt.quiver(
    var_x,
    var_y,
    var_u,
    var_v,
    angles="xy",
    scale_units="xy",
    scale=1,
    color=["r", "g", "b", "g", "r", "y"],
)
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.grid()
plt.show()


# %%NBQA-CELL-SEPfaab7c
vec_a = np.array([1, 2])
vec_b = np.array([4, -1])
vec_c = np.array([3, 5])

vec_d = vec_a + (vec_b + vec_c)
vec_k = vec_b + (vec_c + vec_a)

print(len(vec_d) == len(vec_k))
print(f" (a+(b+c))==(b+(c+a)): \n {(vec_a+(vec_b+vec_c))}{(vec_b+(vec_c+vec_a))}")


# %%NBQA-CELL-SEPfaab7c
vec_a = np.array([5, 4, 3, 1])
vec_b = vec_a * (-1)
print(f"Vector vec_a is opposite to vector vec_b:\n{vec_a}\n{vec_b}")
print(f"Magnitude of vector vec_a equals the one of vec_b: {len(vec_a)}={len(vec_b)}")
print(
    f"The sum of vector vec_a and its opposite vector vec_b equals 0: vec_a+vec_b = {vec_a+vec_b} "
)


# %%NBQA-CELL-SEPfaab7c
vct_a1 = np.array([2, 3, 1, 2])  # subtrahend
vct_a2 = np.array([7, 5, 8, 3])  # minuend
vct_a3 = np.subtract(vct_a2, vct_a1)  # difference : vct_a3 = vct_a2-vct_a1

print(f"minuend - subtrahend = difference \n {vct_a2} - {vct_a1} = {vct_a3}\n")
print(f"minuend = difference  + subtrahend  \n {vct_a3} + {vct_a1} = {vct_a2}")


# %%NBQA-CELL-SEPfaab7c
vec = np.array([1, -2, 3, -4])
print(-1 * vec)


# %%NBQA-CELL-SEPfaab7c
vec = np.array([2, 3])  # a row vector
opposit_vec = -1 * vec
origin = [0], [0]

plt.axis("equal")
plt.grid()

plt.quiver(*origin, *vec, scale=10, color="g")
plt.quiver(*origin, *opposit_vec, scale=10, color="y")
plt.show()


# %%NBQA-CELL-SEPfaab7c
# We'll use a numpy array for our vector
vector = np.array([2, 1])
vector_1 = -1 * vector

# and we'll use a quiver plot to visualize it.
origin = [0], [0]
plt.axis("equal")
plt.grid()
plt.ticklabel_format(style="sci", axis="both", scilimits=(0, 0))
plt.quiver(*origin, *vector, scale=10, color="r")
plt.quiver(*origin, *vector_1, scale=10, color="b")

plt.show()


# %%NBQA-CELL-SEPfaab7c
var_p2 = np.array([4, 5])
var_p1 = np.array([3, 2])

print((var_p2 - var_p1) == (var_p2 + (-1) * var_p1))
print(
    f"{[var_p2[0] -var_p1[0], var_p2[1] -var_p1[1]]}={[var_p2[0] + (-1)* var_p1[0], var_p2[1] +(-1)* var_p1[1]]}"
)


# %%NBQA-CELL-SEPfaab7c
a_no_orientation = np.arange(3)
arr_row = np.array([[-2, 1, -3]])  # row vector
arr_column = np.array([[4], [-2], [7]])  # column vector
arr_zero = np.ones(3)
print("a_no_orientation:", a_no_orientation.shape, a_no_orientation)
print("a_r:", arr_row.shape, arr_row)
print("a_c:", arr_column.shape, "\n", arr_column)
print("a0:", arr_zero.shape, arr_zero)


# %%NBQA-CELL-SEPfaab7c
# Broadcasting is possible only if shapes of operands are equal
print(
    "a_no_orientation * arr_zero:",
    a_no_orientation * arr_zero,
)
print("a_rT *  a0:", arr_row * arr_zero)
print("a_c * a0:", "\n", arr_column * arr_zero)


# %%NBQA-CELL-SEPfaab7c
# Given vectors
vector_a1 = np.array([[-1, 2]])
vector_a2 = np.array([[-2, 3]])  # works
vector_a2 = np.array(
    [[-2, 3, 4]]
)  # operands could not be broadcast together with shapes (1,2) (1,3)


# %%NBQA-CELL-SEPfaab7c
vect_a1 = np.array([[1, 2, 3]])
vect_a2 = vect_a1.T
print(vect_a1, vect_a2)
print(vect_a1.shape, vect_a2.shape)


# %%NBQA-CELL-SEPfaab7c
#  3*a1, 0,5*a2, a1+2*a2, 0,5*a1-a2
sample_b = 3 * vect_a1
sample_c = 0.5 * vect_a2
sample_d = vect_a1 + 2 * vect_a2
sample_e = 0.5 * vect_a1 - vect_a2
print(sample_b, "\n")
print(sample_c, "\n")
print(sample_d, "\n")
print(sample_e)


# %%NBQA-CELL-SEPfaab7c
# # Display row vector ([[]])
v_r = np.array([[2, -1]])  # tail [2,-1]
plt.plot(
    [0, v_r[0][0]], [0, v_r[0][1]]
)  # v[0]- first row, v[0][0] - first row, first column(equals 2),
# v[0][1]]- first row, second column(equals -1)
plt.axis([-2, 2, -2, 2])  # OX(axis=1) (-3, 3), OX(axis=0):(-3, 3)
print(v_r, v_r.shape)


# %%NBQA-CELL-SEPfaab7c
# plt.plot([0, sample_b[0][1]], [0, sample_b[0][1]], color='green')# b marker='o'
# plt.plot([0, sample_d[0][1]], [0, sample_d[0][1]])# d
plt.plot([0, sample_e[0][1]], [0, sample_e[0][1]], color="y", ls="--")  # e
# plt.plot([0, sample_c[0][1]], [0, sample_c[0][1]],color='r')# c
plt.axis([-10, 10, -10, 10])


# %%NBQA-CELL-SEPfaab7c
vect = np.arange(2, 10)
print(vect, vect.shape, "\n", 0 * vect, vect.shape)


# %%NBQA-CELL-SEPfaab7c
# vect_a = np.array([[1, 4]])
vect_a = np.array([[1, 4]]).T
# vect_a = np.array([1, 4])

num_1 = 2
num_2 = 3
print(vect_a, num_1, num_2, sep="\n")


# %%NBQA-CELL-SEPfaab7c
print("(num_1*num_2) * (vect_a) => ", (num_1 * num_2) * vect_a)
print("(num_1) * (num_2*vect_a) => ", num_1 * (num_2 * vect_a))


# %%NBQA-CELL-SEPfaab7c
vct_a = np.array([[1, 4]])
# vct_a = np.array([[1, 4]]).T
# vct_a = np.array([1, 4])
vct_a1 = np.array([4, 5])
vct_a2 = np.array([-2, -1])

letter = -2
letter_1 = 2
letter_2 = 3
# print(vct_a, letter_1, letter_2, sep = '\n')


# %%NBQA-CELL-SEPfaab7c
letter * (vct_a1 + vct_a2) == letter * vct_a1 + letter * vct_a2


# %%NBQA-CELL-SEPfaab7c
(letter_1 + letter_2) * vct_a1 == letter_1 * vct_a1 + letter_2 * vct_a1


# %%NBQA-CELL-SEPfaab7c
# a) a+0,5*(b-a)= 0,5*(a+b)

arrr_a = np.array([[1, 4]])
arrr_b = np.array([[2, 3]])
# arrr_a = np.array([[1, 4]]).T
# arrr_a = np.array([1, 4])
# arrr_a1 = np.array([4, 5])
# arrr_a2 = np.array([-2, -1])

arrr_a + 0.5 * (arrr_b - arrr_a) == 0.5 * (arrr_a + arrr_b)

# arrr_a + 0,5*(arrr_b-arrr_a) = arrr_a + 0,5*arrr_b - 0,5*arrr_a = 0,5*arrr_b + 0,5*arrr_a = 0,5*(arrr_a+arrr_b)


# %%NBQA-CELL-SEPfaab7c
# b) arrr_a- 0.5*(arrr_a+arrr_b) = arrr_a - 0.5*arrr_a - 0.5*arrr_b = 0.5*arrr_a - 0.5*arrr_b = 0.5*(arrr_a-arrr_b)

arrr_a = np.array([[1, 4]])
arrr_b = np.array([[2, 3]])
arrr_a - 0.5 * (arrr_a + arrr_b) == 0.5 * (arrr_a - arrr_b)
