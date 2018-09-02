"""
Course 1
Week 2
Indexing Dataframes (Pandas)
"""

import pandas as pd

# the index is a 'row level' label

# in olympics data we indexed the dataframe by the name of the country

# indices can either be inferred or set explicitly

df = pd.read_csv('csv/olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2] == '01':
        df.rename(columns={col: 'Gold' + col[4:]}, inplace=True)
    if col[:2] == '02':
        df.rename(columns={col: 'Silver' + col[4:]}, inplace=True)
    if col[:2] == '03':
        df.rename(columns={col: 'Bronze' + col[4:]}, inplace=True)
    if col[:1] == '№':
        df.rename(columns={col: '#' + col[1:]}, inplace=True)

# let's index by the number of gold medals won at the summer games

# step 1 - preserve the country data in a separate column

df['country'] = df.index

# step 2 - use set_index to set the index column to gold

df = df.set_index('Gold')

print(df.head())

# we can reset by using reset_index

df = df.reset_index()

print(df.head())  # returns to the default numbered index

# create a new data set

df = pd.read_csv('csv/census.csv')

print(df.head())

# get a list of all the unique values in a given column

print(df['SUMLEV'].unique())  # --> [40 50]

# get rid of summaries at the state level and just keep the county level data

df = df[df['SUMLEV'] == 50]

print(df.head())

# reduce the data to the total pup estimates and total number of deaths

# step 1 - create a list of column names we want to keep

columns_to_keep = ['STNAME',
                   'CTYNAME',
                   'BIRTHS2010',
                   'BIRTHS2011',
                   'BIRTHS2012',
                   'BIRTHS2013',
                   'BIRTHS2014',
                   'BIRTHS2015',
                   'POPESTIMATE2010',
                   'POPESTIMATE2011',
                   'POPESTIMATE2012',
                   'POPESTIMATE2013',
                   'POPESTIMATE2014',
                   'POPESTIMATE2015']

# step 2 - project those and assign the resulting dataframe to our df variable

df = df[columns_to_keep]

print(df.head())

# now load the data and set the index to be a combination of the state and county values

# step 3 - create a list of the column identifiers we want to have indexed
# call set_index with this list

df = df.set_index(['STNAME', 'CTYNAME'])

print(df.head())

print(df.loc['New York', 'Albany County'])

print(df.loc['New York'])

print(df.loc[[('New York', 'Albany County'), ('New York', 'Bronx County')]])
