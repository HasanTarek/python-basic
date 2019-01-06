"""
Data type to store more than one variable name
Dictionary item are in brackets {} in key:value pairs, separated with ","{'k1':'v1','k2':'v2'}
Not sequenced, no index -> Mapping
"""

car = {'make': 'bmw', 'model': '550i', 'year': 2016}
print(car)

print(car['model'])

print(car['make'])

print(car['year'])


d = {}

d['one'] = 1
d['two'] = 2

print(d)

sum_1 = d['two'] + 8
print(sum_1)
print(d)
d['two'] = d['two'] + 8
print(d)

