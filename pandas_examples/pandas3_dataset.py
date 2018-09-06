"""
A Testing Ground for Pandas
"""

import quandl
import pandas as pd


# load your api key

api_key = open('/Users/timothyeason/Desktop/quandlapikey.txt', 'r').read()

df = quandl.get('FMAC/HPI')

print(df.head())

# get the abbreviations for the fifty states

fifty_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

print(fifty_states[0][1][1:])

fifty_states = list(fifty_states[0][1][1:])

print(fifty_states)