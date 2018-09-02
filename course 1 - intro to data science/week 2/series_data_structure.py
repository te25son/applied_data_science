"""
Course 1
Week 2
The Series Data Structure
"""

import pandas as pd
import numpy as np

animals = ['Tiger', 'Lion', 'Bear']
print(pd.Series(animals))

numbers = [1, 2, 3]
print(pd.Series(numbers))

animals = ['Lion', 'Tiger', None]
print(pd.Series(animals))

numbers = [1, 2, None]
print(pd.Series(numbers))  # None is returned as NaN (not a number) by pandas

print(np.nan == None)  # False

print(np.nan == np.nan)  # False

print(np.isnan(np.nan))  # True

sports = {
    'Archery': 'Bhutan',
    'Golf': 'Scotland',
    'Sumo': 'Japan',
    'Taekwondo': 'South Korea'
}
s = pd.Series(sports)
print(s)
print(s.index)

s = pd.Series(['Tiger', 'Lion', 'Bear'], index=['India', 'Angola', 'America'])
print(s)

s = pd.Series(sports, index=['Golf', 'Sumo', 'Hockey'])
print(s)