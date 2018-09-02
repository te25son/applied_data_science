"""
Course 1
Week 2
Querying a Dataframe (Pandas)
"""

import pandas as pd

# BOOLEAN MASKING

# Boolean mask = an array which can be 1D like a series or 2D like a dataframe

# the array is overlaid on top of the data structure we're querying

# any cell aligned with a True value will be added, while thos aligned with False will not

# EXAMPLE

# see only countries who have won a gold medal at the summer olympics

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

print(df['Gold'] > 0)

only_gold = df.where(df['Gold'] > 0)

print(only_gold.head())  # notice the countries that don't meet the criteria have NaN

print(only_gold['Gold'].count())  # --> 100 NaN is not a value, so those countries not counted

print(df['Gold'].count())  # --> 147 counts all countries with a value in gold column

# to get rid of NaN countries, use the dropna method
only_gold = only_gold.dropna()

print(only_gold.head())

# this can be simplified further

# pandas allows the indexing operator to take a boolean mask as a value

# rather than a list of column names

only_gold = df[df['Gold'] > 0]  # No NaNs in dataframe when queried in this manner
print(only_gold.head())

# furthermore, the output of two boolean masks being compared with logical operators

# is another boolean mask

# you can chain together a bunch of and/or statements to create a more complex query

# EXAMPLE

# create a mask for all countries who have received a gold in the summer olympics

# and logically order that with all countries who've received a gold in the winter olympics

print(len(df[(df['Gold'] > 0) | (df['Gold.1'] > 0)]))  # --> 101

# have there been any countries that have won a gold in the winter but not summer olympics?

print(len(df[(df['Gold.1'] > 0) & (df['Gold'] == 0)]))  # --> 1

only_winter_gold = df[(df['Gold.1'] > 0) & (df['Gold'] == 0)]
print(only_winter_gold.head())

only_summer_gold = df[(df['Gold'] > 0) & (df['Gold.1'] == 0)]
print(len(only_summer_gold))  # --> 63
print(only_summer_gold.head())

# write a query to return all of the names of people who bought products worth more than $3.00.
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})

purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})

purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])

over_three = df['Name'][df['Cost'] > 3]
print(over_three)
