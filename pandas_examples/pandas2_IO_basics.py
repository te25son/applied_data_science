"""
Testing Space for Pandas
"""

import pandas as pd


# pandas IO
# IO = Input Output
# you can IO mulitple formats

df = pd.read_csv('csv/zillow77006.csv')

# set index to date column

df.set_index('Date', inplace=True)

print(df.head())

# save the data as a new csv

df.to_csv('csv/new_csv.csv')

# read the created csv back into a df

df = pd.read_csv('csv/new_csv.csv')

print(df.head())

# read the csv again but assign column index

df = pd.read_csv('csv/new_csv.csv', index_col=0)

print(df.head())

# rename the columns
# NOTE : the index is no longer a column

df.columns = ['Houston_HPI']

print(df.head())

# save a new csv

df.to_csv('csv/new_csv2.csv')

# save csv without header / only data

df.to_csv('csv/new_csv3.csv', header=False)

# read the last csv into a dataframe and name the columns

df = pd.read_csv('csv/new_csv3.csv', names=['Date', 'Houston_HPI'], index_col=0)

# read dataframe to html format

df.to_html('html/example.html')

# rename single existing column / leave others as they are

df = pd.read_csv('csv/new_csv3.csv', names=['Date', 'Houston_HPI'])

df.rename(columns={'Houston_HPI': '77006_HPI'}, inplace=True)

print(df.head())  # Date isn't changed

df.rename(columns={'Date': 'YY/MM/DD', '77006_HPI': 'Houston_HPI'}, inplace=True)

print(df.head())
