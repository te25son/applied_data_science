"""
Course 1
Week 1
Functions in Python
"""

# a function that adds two numbers together


def add_numbers(x, y):
    """
    takes integers x and y and returns their sum
    """
    return x + y


print(add_numbers(5, 67))

# adds an optional third parameter to the add_numbers function


def add_numbers(x, y, z=None):
    """
    takes up to three integers and returns their sum
    """
    if z is None:
        return x + y

    else:
        return x + y + z


print(add_numbers(3, 4, 6))
print(add_numbers(4, 66))

# add a flag parameter to the add_numbers function


def add_numbers(x, y, z=None, flag=False):
    """
    takes up to three inegers and a bool value.
    if bool value is True, returns message.
    if bool value is False, returns sum of integers.
    """
    if flag:
        return 'Flag is True!'
    elif z is None:
        return x + y
    else:
        return x + y + z


print(add_numbers(1, 2, 2, True))
print(add_numbers(1, 2, 3))
print(add_numbers(1, 3))

# assign function to a variable

a = add_numbers  # notice the parenthesis are gone when assigning a function to a variable
print(a(1, 2))
