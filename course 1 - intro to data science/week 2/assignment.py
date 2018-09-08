"""
Course 1
Week 2
Assignment
"""

import pandas as pd

# PART 1

# set up

df = pd.read_csv('csv/olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index)
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()


# question 1


def answer_one():
    """
    Returns the country that's won the most gold medals in the summer games
    """
    return df['Gold'].idxmax()


def answer_two():
    """
    Returns the country with the biggest difference between their summer gold medal
    count and their winter gold medal count
    """
    return (df['Gold'] - df['Gold.1']).idxmax()


def answer_three():
    """
    Returns the country with the biggest difference between their summer gold medal
    count and their winter gold medal count relative to their total gold medal count
    """
    df_copy = df.copy()
    df_copy = df_copy[(df_copy['Gold'] > 0) & (df_copy['Gold.1'] > 0)]

    return ((df_copy['Gold'] - df_copy['Gold.1']) / df_copy['Gold.2']).idxmax()


def answer_four():
    """
    Return a series called Points where each gold medal is worth 3, silver 2, and bronze 1
    """
    df['Points'] = df['Gold.2']*3 + df['Silver.2']*2 + df['Bronze.2']

    return df['Points']


# PART 2

# set up

census_df = pd.read_csv('csv/census.csv')


def answer_five():
    """
    Return the State with the most counties in it
    """
    return census_df['STNAME'].value_counts().idxmax()


def answer_six():
    """
    Return the three most populous states from highest to lowest
    """
    df_copy = census_df.copy()
    df_copy = df_copy.groupby('STNAME')
    states_pop = pd.DataFrame(columns=['Pop'])

    for idx, col in df_copy:
        states_pop.loc[idx] = [
            col.sort_values(by='CENSUS2010POP', ascending=False)[1:4]['CENSUS2010POP'].sum()
        ]

    states_pop.sort_values(by='Pop', ascending=False, inplace=True)

    return states_pop.index.tolist()[:3]


def answer_seven():
    """
    Return the county with the largest absolute population change between 2010 - 2015
    """
    df = census_df[
        ['STNAME',
         'CTYNAME',
         'POPESTIMATE2015',
         'POPESTIMATE2014',
         'POPESTIMATE2013',
         'POPESTIMATE2012',
         'POPESTIMATE2011',
         'POPESTIMATE2010']
    ]

    df = df[df['STNAME'] != df['CTYNAME']]

    print(df.head())

    index = (df.max(axis=1) - df.min(axis=1)).idxmax()

    return census_df.loc[index]['CTYNAME']


def answer_eight():
    return census_df[
        (census_df['REGION'] < 3) &
        (census_df['CTYNAME'] == 'Washington County') &
        (census_df['POPESTIMATE2015'] > census_df['POPESTIMATE2014'])
    ][['STNAME', 'CTYNAME']]
