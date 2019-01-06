"""
Examples to show how string formatting works in python
"""

city = "nyc"
event = "show"
print("Welcome to " + city + " and enjoy the " + event)
print("Welcome to %s" % city)
print("Welcome to %s and enjoy the %s" % (city, event))


a = "one two three"
print(a.split())


a = "This is a string"
# print(a[:1])
# print(a[:])
# print("**********")
# print(a[:1])
# print(a[:2])
# print("**********")
# print(a[1:8])
# print(a[0:2])
# print(a[:])
# print(a[:6])

# print(a[:-4])
# print(a[:-2])
# print(a[-2:])
# print(a[-1:])

# print(a[4::])
print(a[::--1])
# print(a[1::3])
# print(a[1::-3])
# print(a[::])
# print(a[-2::])


