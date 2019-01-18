a = 1
b = 2

if a < b:
    print("a is less than b")
    print("a is definitely less than b")
print("Not sure if a is less than b")

print("*" * 30)

c = 5
d = 4

if c < d:
    print("c is less than d")
else:
    print("c is NOT less than d")
    print("i do not think c is less than d")
print("out side the if block")

print("*" * 30)

e = 20
f = 8

if e < f:
    print("e is less than f")

elif e == f:
    print("e is equal to f")
elif e > f + 10:
    print("e is greater than f by more than 10")
else:
    print("e is greater than then f")

print("*" * 30)

g = 10
h = 10

if g < h:
    print("g is less than h")
else:
    if g == h:
        print("g is equal to h")
    else:
        print("g is greater than h")

print("*" * 30)

x = 21
y = 10

if x < y:
    print("x is grater than y")

elif x == y:
    print("x is equal to y")
elif x > y + 10:
    print("x is grater than y by 10")

else:
    print("x is less than y")

print("*" * 30)

name = "hasan"
height_m = 2
weight_kg = 90

bmi = weight_kg / (height_m**2)

if bmi < 25:
    print(name)
    print("is not over weight")
else:
    print(name)
    print("is over weight")

print("*" * 30, "practice", "*" * 30)

name = "titu"
height = 2
weight_kg = 90
bmi = weight_kg / (height**2)

if bmi < 25:
    print(name)
    print("is not over weight")
else:
    print(name)
    print("is over weight")







