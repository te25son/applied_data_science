"""
Course 1
Week 3
Merging Dataframes (Pandas)
"""

import pandas as pd

df = pd.DataFrame(
    [{'Name': 'Chris', 'Item Purchased': 'Sponge', 'Cost': 22.50},
     {'Name': 'Kevyn', 'Item Purchased': 'Kitty Litter', 'Cost': 2.50},
     {'Name': 'Filip', 'Item Purchased': 'Spoon', 'Cost': 5.00}],
    index=['Store 1', 'Store 1', 'Store 2']
)

print(df)

# if the list is as long as the dataframe this is okay
df['Date'] = ['December 1', 'January 1', 'May 15']

# using a scaler value is also okay and will assign to every row
df['Delivered'] = True

# if we don't know or have a value, we can manually add it as None
df['Feedback'] = ['Postive', None, 'Negative']

adf = df.reset_index()

# insert values into specific areas without having to provide a value for each row
# use a series

adf['Date'] = pd.Series(
    {0: 'December 5', 2: 'January 1'}  # note that you MUST reset the index for this
)

print(adf)

##
#
# joining two dataframes
#
##

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])
staff_df = staff_df.set_index('Name')
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
student_df = student_df.set_index('Name')
print(staff_df.head())
print()
print(student_df.head())
print()

# get the union of these
print(pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True))
print()

# get the intersection
print(pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True))
print()

# get all staff ("left join" because staff is on the left)
print(pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True))
print()

# get all students (right join)
print(pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True))

print()
print()

# other interesting parameters...

# you don't need to use indices to join on. you can use columns as well...

staff_df = staff_df.reset_index()
student_df = student_df.reset_index()

print(pd.merge(staff_df, student_df, how='outer', left_on='Name', right_on='Name'))

##
#
# conflict between dataframes
#
##

staff_df = pd.DataFrame(
    [{'Name': 'Kelly', 'Role': 'Director of HR', 'Location': 'State Street'},
     {'Name': 'Sally', 'Role': 'Course liasion', 'Location': 'Washington Avenue'},
     {'Name': 'James', 'Role': 'Grader', 'Location': 'Washington Avenue'}]
)
student_df = pd.DataFrame(
    [{'Name': 'James', 'School': 'Business', 'Location': '1024 Billiard Avenue'},
     {'Name': 'Mike', 'School': 'Law', 'Location': 'Fraternity House #22'},
     {'Name': 'Sally', 'School': 'Engineering', 'Location': '512 Wilson Crescent'}]
)

print(pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name'))
print()

products_df = pd.DataFrame(
    {'ProductID': [4109, 1412, 8391],
     'Price': [5.0, 0.5, 1.5],
     'Product': ['Sushi Roll', 'Egg', 'Bagel']}
).set_index('ProductID')

invoices_df = pd.DataFrame(
    {'Customer': ['Ali', 'Eric', 'Ande', 'Sam'],
     'ProductID': [4109, 1412, 8391, 4109],
     'Quantity': [1, 12, 6, 2]}
)

print(pd.merge(products_df, invoices_df, left_index=True, right_on='ProductID'))
print()
print(pd.merge(products_df, invoices_df, how='outer', left_on='ProductID', right_on='ProductID'))

