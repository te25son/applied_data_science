"""
Testing Space for Pandas
"""

import pandas as pd
import numpy as np

web_stats = {
    'Day': [1, 2, 3, 4, 5, 6],
    'Visitors': [60, 34, 55, 36, 70, 52],
    'Bounce Rate': [65, 72, 66, 59, 71, 62]
}

# convert dictionary to dataframe

df = pd.DataFrame(web_stats)

print(df.head())
print(df.head(2))
print(df.tail())
print(df.tail(2))

# if you don't specific an index
# everything is treated as a separate column

# set an index

print(df.set_index('Day'))

print(df.head())  # notice we lost the index we assigned

print('')

# three ways to change the data layout

# df = df.set_index('Days')
# df2 = df.set_index('Days')
# df.set_index('Days', inplace=True)

# reference a specific column

print(df['Visitors'])
print(df.Visitors)

# reference multiple columns

print(df[['Bounce Rate', 'Visitors']])

# convert a column to a list

print(df.Visitors.tolist())

# can you convert multiple columns to a list??

# NOT WITH PANDAS

# for example...

# print(df[['Visitors', 'Bounce Rate']].tolist())  # NO NO. treated as an array

# HOWEVER

# you can use numpy to convert this to an array :-)

print(np.array(df[['Bounce Rate', 'Visitors']]))  # BOOM!

print(np.array(df.Visitors))

print('')

# and what about this...

df2 = pd.DataFrame(np.array(df[['Bounce Rate', 'Visitors']]))

print(df2)  # Oh hell yeah you can arrays into a pandas dataframe!!
