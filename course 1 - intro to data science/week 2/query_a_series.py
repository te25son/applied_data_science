"""
Course 1
Week 2
Querying a Series (Pandas)
"""

import pandas as pd
import numpy as np

sports = {
    'Archery': 'Bhutan',
    'Golf': 'Scotland',
    'Sumo': 'Japan',
    'Taekwondo': 'South Korea'
}

s = pd.Series(sports)

# to find the third element in the series

print(s.iloc[3])

# to get the index value of a key

print(s.loc['Golf'])

s = pd.Series([100.00, 120.00, 101.00, 3.00])
print(s)

total = 0
for item in s:
    total += item
print(total)

# or you can use numpy and pass s as the iterable

total = np.sum(s)  # this is significantly faster than using the above for loop
print(total)

s = pd.Series(np.random.randint(0, 1000, 10000))
print(len(s))

print(s.head())  # head prints out the first 5 items in a series by default

# you can add to every item in a series quickly. for example...
s += 2  # adds 2 to every item in a series
print(s.head())

# the above example is much faster than this example doing the same thing...
# i hid it because it's too slow.
# for label, value in s.iteritems():
#     s.loc[label] = value + 2
#
# print(s.head())

# you can add items to a series using the .loc operator
s = pd.Series([1, 2, 3])
s.loc['Animal'] = 'Bear'
print(s)

# we can append series to other series
original_sports = pd.Series(sports)

cricket_loving_countries = pd.Series(
    ['Australia', 'Barbados', 'Pakistan', 'England'],
    index=['Cricket', 'Cricket', 'Cricket', 'Cricket']
)
print(cricket_loving_countries)

# NOTE: the append method doesn't change the underlying series
all_countries = original_sports.append(cricket_loving_countries)
print(all_countries)
print(cricket_loving_countries)
print(original_sports)
