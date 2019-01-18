# def function():
#     print("hi")
# function()


# def function(x):
#     print(x)
#     return x * 2
#
#
# q = function(3)
#
# print("*" * 30)
#
#
# def function_10(x, y):
#     return x + y
#
#
# d = function_10(2, 5)
# print(d)
#
#
# def function(a, b):
#     return a + b
#
#
# c = function(1, 5)
# print(c)

#
# def function(x, y):
#     return x * y
#
# a = function(2, 4)
# print(a)


# def function(x):
#     return x * 3
# a = function(2)
# print(a)
#
# b = function(5)
# print(b)
#
# c = function(6)
# print(c)


# def function():
#     print("love" + " you" + " hasan")
#
#
# function()


# def function(x):
#     print(x)
#
#
# a = function(2)
#
#
# def function(y):
#     return y + 3
#
#
# print(function(2))
#
#
# def function(z, r):
#     return z + r
#
#
# print(function(2, 3))

# q = function(2, 400)
# print(q)

# def function():
#     print("fig")
#     print("figgggggg")
# function()

# def function(x, r):
#     return x * r
#
#
# # print(function(3, 4))
#
# p = function(3, 4)
# print(p)

# def function(d):
#     return d - 5
# print(function(13))
#
# def function(full):
#     print(full)
#     print("halal")
# function(4)

# def function(www):
#     print(www)
#     print("hasab")
# function(3)
#
# def function(x):
#     print(x)
#     print("still in the function")
#     return 3 * x
# print(function(4))

#
# def function(y):
#     print(y)
#     return y + 5
#
#
# g = function(10)
# print(g)

name_1 = "titu"
height_1 = 2
weight_kg_1 = 110

name_2 = "kalu"
height_2 = 3
weight_kg_2 = 90

name_3 = "sad"
height_3 = 1
weight_kg_3 = 84


def bmi_calculater(name, height, weight_kg):
    bmi = weight_kg / (height ** 2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " not overweight"
    else:
        return name + " is over weight"


return1 = bmi_calculater(name_1, height_1, weight_kg_1)
return2 = bmi_calculater(name_2, height_2, weight_kg_2)
return3 = bmi_calculater(name_3, height_3, weight_kg_3)

print(return1)
print(return2)
print(return3)
