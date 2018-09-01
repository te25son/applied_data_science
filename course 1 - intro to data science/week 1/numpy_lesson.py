"""
Course 1
Week 1
Intro to Numpy
"""

import numpy as np

# create an array
my_list = [1, 2, 3]
x = np.array(my_list)
print(x)

y = np.array([4, 5, 6])
print(y)

# make a multidimensional array by passing a list of lists
m = np.array([[7, 10, 11], [1, 5, 6]])
print(m)

# check the dimensions of our array using the shape attribute
print(m.shape)

# for the arange function, we pass in a start, a stop, and a step size,
# and it returns evenly spaced values within a given interval
n = np.arange(0, 30, 2)
print(n)

# you can reshape an array
n = n.reshape(3, 5)
print(n)

# the linspace function is similar to arange, except we tell it how many
# numbers we want returned, and it will split up the interval accordingly.
o = np.linspace(0, 4, 9)  # returns 9 evenly spaced values from 0 - 4
print(o)

o.resize(3, 3)
print(o)

# ones returns a new array of given shape and type, filled with ones.
print(np.ones((2, 3)))

# zeros returns a new array of given shape and type, filled with zeros.
print(np.zeros((2, 3)))

# eye returns a 2-D array with ones on the diagonal and zeros elsewhere.
print(np.eye(3))

# diag extracts a diagonal or constructs a diagonal array.
print(np.diag(y))

# Create an array using repeating list
print(np.array([1, 2, 3] * 3))

# repeat elements using repeat
print(np.repeat([1, 2, 3], 3))

# combine arrays
p = np.ones([2, 3], int)
print(p)

# use vstack to stack arrays in sequence vertically (row wise)
print(np.vstack([p, 2*p]))

# use hstack to stack arrays in sequence horizontally (column wise)
print(np.hstack([p, 2*p]))

###########################

# Operations

###########################

print(x + y)  # elementwise addition     [1 2 3] + [4 5 6] = [5  7  9]
print(x - y)  # elementwise subtraction  [1 2 3] - [4 5 6] = [-3 -3 -3]

print(x * y)  # elementwise multiplication  [1 2 3] * [4 5 6] = [4  10  18]
print(x / y)  # elementwise divison         [1 2 3] / [4 5 6] = [0.25  0.4  0.5]

print(x**2)  # elementwise power  [1 2 3] ^2 = [1 4 9]

print(x.dot(y))  # dot product  1*4 + 2*5 + 3*6

z = np.array([y, y**2])
print(len(z))  # number of rows of array

r = np.arange(36)
r.resize((6, 6))
print(r)

