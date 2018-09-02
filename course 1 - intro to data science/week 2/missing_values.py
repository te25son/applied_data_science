"""
Course 1
Week 2
Missing Values (Pandas)
"""

import pandas as pd

df = pd.read_csv('csv/log.csv')

print(df.head())

df = df.set_index('time')

df = df.sort_index()

print(df.head())

# the timestamp is repeated multiple times
# let's create a subindex to help us further understand the data

df = df.reset_index()

df = df.set_index(['time', 'user'])

print(df.head())

df = df.fillna(method='ffill')

print(df.head())
