'''
Nested Dictionary:
d = {'k1': {'nestK1': 'nestvalue1', 'nestk2': 'nestvalue2'}}
'''

cars = {'audi': {'year': 2016, 'type': 'sports'}, 'honda': {'year': 2018, 'type': 'coupe'}}

honda_year = cars['honda']['year']
print(honda_year)
audi_year = cars['audi']['year']
print(audi_year)

print("*" * 30)

birds = {'love_bird': {'place': 'Africa', 'type': 'Small'}, 'ostrich': {'country': 'Guatemala', 'type': 'Big'}}
new_bird = birds['ostrich']['type']
old_bird = birds['love_bird']['place']
print(new_bird)
print(old_bird)

print("*" * 30)

'''Given a nested dictionary d={"key1": [1, 2, 3], "key2": [4, 5, 6], "key3": [7, 8, 9]}.

What is the output of d["key1"][2]?'''

d = {"key1": [1,2,3], "key2":[4,5,6], "key3": [7,8,9]}
print(d)
new = d["Key1"][2]
print(new)
print("[***********UNSOLVED***********]")


