"""
Course 1
Week 1
Date and Time in Python
"""

import datetime as dt
import time as tm


print(tm.time())  # returns the time in seconds since January 1, 1970

# convert the above timestamp to current time:
dt_now = dt.datetime.fromtimestamp(tm.time())
print(dt_now)

# get the year
print(dt_now.year)

# get the month
print(dt_now.month)

# get the day
print(dt_now.day)

# get the hour, minute and second
print(dt_now.hour, dt_now.minute, dt_now.second)

# timedelta is a duration expressing the difference between two dates
delta = dt.timedelta(days=100)
print(delta)

today = dt.datetime.today()
print(today)

print(today - delta)  # returns the date 100 days ago

print(today > today - delta)  # compares date
