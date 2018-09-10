"""
Course 1
Week 3
Pandas Idioms
"""

import pandas as pd
import numpy as np

# there are many solutions to an issue in programming
# however there are some solutions that are more appropriate
#
# these are called idiomatic solutions


file = 'csv/census.csv'

df = pd.read_csv(file)

print(df.head())
print()

print(df.where(df['SUMLEV'] == 50)
        .dropna()
        .set_index(['STNAME', 'CTYNAME'])
        .rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})
        .head())

# create a series object to get the min and max values of 5 population rows


def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    return pd.Series({'min': np.min(data), 'max': np.max(data)})


print(df.apply(min_max, axis=1)
        .head())


# create a series object to return INTO the existing dataframe
# the new columns will contain the min and max values found in
# the pre-existing columns that contain

def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    row['max'] = np.max(data)
    row['min'] = np.min(data)
    return row


print(df.apply(min_max, axis=1)
        .head())


# use lambda to perform the above tasks

rows = [
    'POPESTIMATE2010',
    'POPESTIMATE2011',
    'POPESTIMATE2012',
    'POPESTIMATE2013',
    'POPESTIMATE2014',
    'POPESTIMATE2015'
]

print(df.apply(lambda x: np.max(x[rows]), axis=1)
        .head())

print()

print(df.apply(lambda x: np.min(x[rows]), axis=1)
        .head())
