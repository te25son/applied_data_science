"""
Course 1
Week 1
Lambda and List Comprehension
"""

my_function = lambda a, b, c: a+b

print(my_function(1, 2, 3))

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']


def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

# option 1


for person in people:
    print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))

# option 2
print(
    list(map(split_title_and_name, people)) == list(map(
    lambda person: person.split()[0] + ' ' + person.split()[-1], people)
    )
)

# create a list of numbers between 1 and 1000
even_list = []

for num in range(0, 1000):
    if num % 2 == 0:
        even_list.append(num)

print(even_list)
print('')

# turn this into a list comprehension

even_list = [num for num in range(0, 1000) if num % 2 == 0]
print(even_list)


def times_tables():
    lst = []
    for i in range(10):
        for j in range(10):
            lst.append(i*j)
    return lst


print(
    times_tables() == [
        (i*j) for i in range(10) for j in range(10)
    ]
)

lowercase = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
digits = '0123456789'
chars = '~!@#$%^&*()_+'

user_ids = [a+b+c+d+e for a in lowercase for b in lowercase for c in digits for d in digits for e in chars]
print(user_ids[:1000])
print(len(user_ids))
