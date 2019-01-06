"""
Tuple Like list but are immutable
It means you can't change them
"""

my_list = [1,2,3]
print(my_list)

my_list[0] = 0
print(my_list)

my_tuple = (1,2,3)
print(my_list)

# my_tuple[0] = 4
# print(my_tuple)
print("********** tuple can not be changed **********")

print(my_tuple[1])
print(my_tuple[1:])
print(my_tuple.count(3))
print(my_tuple.index(2))
print("*"*30)

t = (10,20,30)
print(t.index(20))








