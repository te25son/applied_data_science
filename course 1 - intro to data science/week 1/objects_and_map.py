"""
Course 1
Week 1
Objects and Map Function in Python
"""

# an example of a class in python


class Person:
    department = 'School of Information'

    uni_name = 'University of Whatever'

    def set_name(self, new_name):
        self.name = new_name

    def set_location(self, new_location):
        self.location = new_location


person = Person()
person.set_name('Chris Webber')
person.set_location('Ann Arbor, MI, USA')

print('{} lives in {} and works in the {} at the {}.'.format(
    person.name, person.location, person.department, person.uni_name
))
print('')

#######################################

# map(func, iter1, ...)
#
# return an iterator that applies 'function' to every item in iterable,
# yielding the results. if additional iterable arguments are passed, function
# must take that many arguments and is applied to the items from all
# iterables in parallel. with multiple iterables, the iterator stops when
# the shortest iterable is exhausted. for cases where the function inputs are
# already arranged int argument tuples, see itertools.starmap()

#######################################

# compare prices for the same items in two different stores
store1 = [10, 11, 12.34, 15]
store2 = [9, 11.1, 12.34, 14.5]
cheapest = map(min, store1, store2)
print(cheapest)

# to see the items in the map object use a for loop
for item in cheapest:
    print(item)

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']


def split_title_and_name(person):
    title = person.split(' ')[0]
    lastname = person.split(' ')[-1]
    return '{} {}'.format(title, lastname)


print(list(map(split_title_and_name, people)))
