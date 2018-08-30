"""
Course 1
Week 1
Types and Sequences in Python
"""

# use 'type' to return an objects type

print(
    type('what is this?'),      # string ('str')
    type(1),                    # integer ('int')
    type(1.0),                  # float
    type(False),                # boolean value ('bool')
    type([1, 2, 3])             # list
)

# tuples are an immutable data structure (immutable = cannot be altered)

tup = ()
print(tup)
tup = (1, 'a', 2, 3)
print(tup)

# lists are a mutable data structure (mutable = can be altered)

a_list = []
print(a_list)
a_list = [1, 3, 6, 7, 9]
print(a_list)

# use append to append an object to the end of a list

a_list.append(22)
print(a_list)

# you can use a 'loop' to loop through the items in a list
# this is an example of a 'for' loop

for num in a_list:
    print(num)

# list comprehension with for loop that adds two to each number in the list

a_list = [num + 2 for num in a_list]
print(a_list)

# you can also you an index operator and a while loop

i = 0
while i != len(a_list):
    print(a_list[i])
    i += 1

# use '+' to concatenate (link together) lists

a = [1, 2]
b = [3, 4]
print(a+b)

# use '*' to repeat lists

print(a*3)

# use 'in' to check if something is inside a list

print(3 in a)  # False
print(2 in a)  # True


##################################

# STRINGS #

##################################


a = 'this is a string'
print(a[0])  # prints the first character in the string
print(a[0:1])  # prints the first character in the string. starts at 0 and goes up to but not including the second num
print(a[2:])  # prints the string starting at index 2 and going to the end
print(a[:4])  # starts at the first character and goes up to but not including the second index value given

firstname = 'Christopher'
lastname = 'Brooks'

print(firstname + ' ' + lastname)
print(firstname*3)
print('Chris' in firstname)

# the split function returns a list object and a parameter detailing where each split is meant to happen
# in the example below, I've split a string at each instance of a space (' ')

firstname = 'Christopher Arthur Hansen Brooks'.split(' ')[0]  # [0] selects the first element of the list
lastname = 'Christopher Arthur Hansen Brooks'.split(' ')[-1]  # [-1] selects the last element of the list
print(firstname)
print(lastname)

name = 'Timothy Eason'
firstname = name.split(' ')[0]
lastname = name.split(' ')[1]
print(firstname)
print(lastname)


##################################

# DICTIONARIES #

##################################


# example of a dictionary
# dictionary = {key : value}

x = {
    'Batman': 'Bruce Wayne',
    'Superman': 'Clark Kent',
    'Spiderman': 'Peter Parker',
    'Iron Man': 'Tony Stark'
}

# retrieve values by calling the name of a dictionary with the key in brackets

print(x['Batman'])  # Bruce Wayne

# you can iterate over the keys of a dictionary with a for loop

for hero in x:
    print(hero)

# use the values module to iterate over values

for name in x.values():
    print(name)

# use items it iterate over both keys and values

for hero, name in x.items():
    print(hero, 'is', name)


##################################

# Unpack Sequences and Formatting #

##################################


# we can unpack sequences into separate variables

my_list = ['hello', 'bonjour', 'ciao', 'ahoj', 'privyet']
english, french, italian, czech, russian = my_list

print(english)
print(french)
print(italian)
print(czech)
print(russian)

sales_record = {
    'price': 4.25,
    'num_items': 5,
    'name': 'Fred'
}

sales_statement = '{} purchased {} item(s) at ${} each for a total of ${}'

print(
    sales_statement.format(
        sales_record['name'],
        sales_record['num_items'],
        sales_record['price'],
        sales_record['num_items']*sales_record['price']
    )
)
