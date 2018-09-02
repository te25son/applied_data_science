"""
Course 1
Week 2
Dataframe Indexing and Loading (Pandas)
"""

import pandas as pd
import csv

# common workflow:

# step 1 - read data into DataFrame

# step 2 - reduce this DataFrame to the specific rows and columns you're interested in working with

# NOTE : any changes you make to your custom DataFrame may have an impact on the original data...

purchase1 = pd.Series({'Name': 'Chris',
                       'Item Purchased': 'Dog Food',
                       'Cost': 22.50})

purchase2 = pd.Series({'Name': 'Kevin',
                       'Item Purchased': 'Kitty Litter',
                       'Cost': 5.00})


purchase3 = pd.Series({'Name': 'Marco',
                       'Item Purchased': 'Coffee Beans',
                       'Cost': 8.75})

df = pd.DataFrame([purchase1, purchase2, purchase3],
                  index=['Store 1', 'Store 1', 'Store 2'])

df['Location'] = None

costs = df['Cost']

print(costs)

# use 'broadcasting' to increase the costs
costs += 2

print(costs)

print(df)  # the bases data has been changed

with open('csv/olympics.csv') as csvfile:
    medals = list(csv.DictReader(csvfile))

for row in medals[:5]:
    print(row)

# do this in pandas
df = pd.read_csv('csv/olympics.csv')
print(df.head())

# use specific parameters to get the data you want
df = pd.read_csv('csv/olympics.csv', index_col=0, skiprows=1)
print(df.head())

# CLEANING THE DATA
# get the column names
print(df.columns)

# rename them using the rename method in pandas
for col in df.columns:
    if col[:2] == '01':
        df.rename(columns={col: 'Gold' + col[4:]}, inplace=True)
    if col[:2] == '02':
        df.rename(columns={col: 'Silver' + col[4:]}, inplace=True)
    if col[:2] == '03':
        df.rename(columns={col: 'Bronze' + col[4:]}, inplace=True)
    if col[:1] == '№':
        df.rename(columns={col: '#' + col[1:]}, inplace=True)

print(df.head())
