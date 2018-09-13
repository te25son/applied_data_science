"""
Course 1
Week 3
Group By (Pandas)
"""

import pandas as pd
import numpy as np

df = pd.read_csv('csv/census.csv')

print(df.head())
print()

# exclude the rows that have a SUMLEV of 40

df = df[df['SUMLEV'] == 50]

print(df.head())
print()

for state in df['STNAME'].unique():
    avg = np.average(df.where(df['STNAME'] == state).dropna()['CENSUS2010POP'])
    print(
        'Counties in {} have an average population of {}'.format(state, str(avg))
    )

print()

# using the groupby method, this process will be much quicker

for group, frame in df.groupby('STNAME'):
    avg = np.average(frame['CENSUS2010POP'])
    print(
        'Counties in {} have an average population of {}'.format(group, str(avg))
    )

# you can provide a function to groupby
# this will segment your data

# split
# apply
# combine

# build a summary data frame for the average population per state in 2010

print(df.groupby('STNAME').agg({'CENSUS2010POP': np.average}))
print()

# build a summary data with the number of counties in each state

print(df.groupby('STNAME').agg({'CENSUS2010POP': np.size}))
print()

adf = pd.DataFrame(
    {
        'Items': ['spectacles', 'testicles', 'wallet', 'watch'],
        'Quantity': [1, 2, 1, 1],
        'Weight (oz.)': [10, 100, 200, 500]
    }
)

print(adf.groupby('Items').apply(lambda gb, a, b: sum(gb[a] * gb[b]), 'Quantity', 'Weight (oz.)'))
print()

# groupby returns two types: a dataframe and a series
# example...

print(type(df.groupby(level=0)['POPESTIMATE2010', 'POPESTIMATE2011']))  # dataframe
print()
print(type(df.groupby(level=0)['POPESTIMATE2010']))  # series
print()

print(
    df.set_index('STNAME')                      # convert df to series with STNAME as index
    .groupby(level=0)['CENSUS2010POP']          # and the 2010 census pop as the only column
    .agg({'avg': np.average, 'sum': np.sum})    # use agg to apply two functions to the column
)

# do the same thing with a series

print(
    df.set_index('STNAME')
    .groupby(level=0)['POPESTIMATE2010', 'POPESTIMATE2011']
    .agg({'avg': np.average, 'sum': np.sum})
)
