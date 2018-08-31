"""
Course 1
Week 1
Reading and Writing CSV Files
"""

import csv

# %precision 2
# above code uses ipython magic to convert all floating point numbers to 2 decimal spaces


with open('csv/mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))

# print the first 3 items in our list
print(mpg[:3])

print(len(mpg))

# get the column names of our csv file
print(mpg[0].keys())
print('')

# find the average city fuel economy across all cars.
# all values in the dictionaries are strings, so we need to convert to float.

print(
    sum(float(d['cty']) for d in mpg) / len(mpg)  # --> 16.858974358974358
)

# find the average highway fuel economy across all cars

print(
    sum(float(d['hwy']) for d in mpg) / len(mpg)  # --> 23.44017094017094
)
print('')

# use set to return the unique values for the number of cylinders the cars have
cylinders = set(d['cyl'] for d in mpg)
print(cylinders)


# group the cars by number of cylinders, and find the average city mpg for each group.
CtyMpgByCyl = []

# iterate over all cylinder levels
for c in cylinders:
    sum_mpg = 0
    cyl_typ_count = 0

    # iterate over all dictionaries
    for d in mpg:

        # if the cylinder type matches
        if d['cyl'] == c:

            # add the city mpg
            sum_mpg += float(d['cty'])
            cyl_typ_count += 1

    # append tuple to CtyMpgByCyl ('cylinder', 'average mpg')
    CtyMpgByCyl.append((c, sum_mpg / cyl_typ_count))

CtyMpgByCyl.sort(key=lambda x: x[0])
print(CtyMpgByCyl)
print('')

# get the class types for each vehicle
vehicle_class = set(d['class'] for d in mpg)
print(vehicle_class)

# find the average highway mpg for each class of vehicle in our dataset
HwgMpgByClass = []

for c in vehicle_class:
    sum_mpg = 0
    vclass_count = 0
    for d in mpg:
        if d['class'] == c:
            sum_mpg += float(d['hwy'])
            vclass_count += 1

    HwgMpgByClass.append((c, sum_mpg / vclass_count))

HwgMpgByClass.sort(key=lambda x: x[1])
print(HwgMpgByClass)

# compare the above to city mpg by class
CtyMpgByClass = []

for c in vehicle_class:
    sum_mpg = 0
    vclass_count = 0
    for d in mpg:
        if d['class'] == c:
            sum_mpg += float(d['cty'])
            vclass_count += 1

    CtyMpgByClass.append((c, sum_mpg / vclass_count))

CtyMpgByClass.sort(key=lambda x: x[1])
print(CtyMpgByClass)
