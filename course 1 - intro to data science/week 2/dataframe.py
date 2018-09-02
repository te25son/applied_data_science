"""
Course 1
Week 2
DataFrame Data Structures (Pandas)
"""

# used for data cleaning and analysis

import pandas as pd

purchase1 = pd.Series({'Name': 'Chris',
                       'Item Purchased': 'Dog Food',
                       'Cost': 22.50})

purchase2 = pd.Series({'Name': 'Kevin',
                       'Item Purchased': 'Kitty Litter',
                       'Cost': 5.00})


purchase3 = pd.Series({'Name': 'Marco',
                       'Item Purchased': 'Coffee Beans',
                       'Cost': 8.75})

# feed into dataframe
df = pd.DataFrame([purchase1, purchase2, purchase3],
                  index=['Store 1', 'Store 1', 'Store 2'])

print(df)  # it makes it pretty for you :-)

# use the .loc operator to get one element of the dataframe
print(df.loc['Store 2'])
print(df.loc['Store 1'])

# check the type
print(type(df.loc['Store 1']))

# NOTE: the indices and column names along either access can be non-unique
# in the above example, we see two purchase records for Store 1 as diff rows

# get a list of all items that have been purchased (regardless of store and by whom)
items = df['Item Purchased']
print(items)

# you can quickly select data based on multiple axes
print(df.loc['Store 1', 'Cost'])
print(df.loc['Store 1', 'Name'])
print(df.loc['Store 2', 'Item Purchased'])
print(df.loc['Store 1', 'Item Purchased'])

# what if we just want to do column selection??
# get a transpose of the dataframe

print(df.T)  # transposes the data so the column names are the row names and vice versa

print(df.T.loc['Cost'])

print(df.loc['Store 1']['Cost'])

# .loc supports slicing!
print(df.loc[:, ['Name', 'Cost']])
print(df.iloc[-1])
print('')

# delete data using drop
print(df.drop('Store 1'))  # returns a dataframe without the dropped items (doesn't affect the underlying df)
print(df)

# in order to change the dataframe permanently, we'll have to make a copy
df_copy = df.copy()
df_copy = df_copy.drop('Store 1')
print(df_copy)

# we can also drop a column
# this way take immediate effect on the dataframe

del df_copy['Name']
print(df_copy)

# and add a column
df['Location'] = None
print(df)

# add a discount of 20% to all costs in the df
df['Cost'] *= 0.80
print(df)
