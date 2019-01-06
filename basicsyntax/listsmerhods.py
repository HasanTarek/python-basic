"""
Built-in methods to help monitoring a list
"""

cars = ["bmw", "honda", "audi"]

length = len(cars)
print(length)

cars.append("Benz")
print(cars)

cars.insert(1, "jeep")
print(cars)

x = cars.index("honda")

print(x)

y = cars.pop()
print(y)
print(cars)

cars.remove("jeep")
print(cars)

slicing = cars[0:2]
a = cars[1:]
print(slicing)
print(a)

print("*" * 20)
print(cars)
cars.sort()
print(cars)

print("########################################")

heroes = ["Hasan", "John", "ahalid"]
length = len(heroes)

print(heroes)
print(length)

heroes.append("thor")
print(heroes)

heroes.insert(2, "zaman")
print(heroes)

x = heroes.index("zaman")
print(x)

y = heroes.pop()
print(y)

heroes.remove("zaman")
print(heroes)

slicing = heroes[1:2]
a = heroes[1:]
print(slicing)
print(a)
print("*" * 20)
print(heroes)
heroes.sort()
print(heroes)

print("*" * 20)

I = [1, 2, 3, 1, 2, 2]
print(len(I))

l = [1, 2, 3, 3, 2, 1]
print(l[-2:])
print(l[4:])
print(l[4:6])

print("*" * 20)
animals = ["cat", "cow", "goat"]
print(animals[0])

print("*" * 20)
sports = ["football", "cricket", "boxing"]
# print(sports[1])

# sports[2] = "kick boxing"
print(sports.pop())

print(sports)
sports[0] = "hand ball"
print(sports)
q = len(sports)
a = list(sports)
print(q)
print(a)
sports.insert(2, "apple")
print(sports)

l = [1, 2, 3, 2, 1, 2]

l.count(1)
print(l.count(1))

l = [1, 2, 3, 1, 2, 2]

a = len(l)
print(a)

l = [1, 1, 3, 3, 2, 1]

# print(l[4:])
# print(l[-2:])
# print(l[4:6])
# print(l[2:6])

l.reverse()

print(l)
