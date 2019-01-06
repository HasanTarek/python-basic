car = {'make': 'bmw', 'model':'550i', 'year':2016}
cars = {'bmw': {'model':'550i', 'year':2016}, 'benz':{'model': 'E350', 'year': 2015}}
print(car.keys())
print(cars.keys())
print(cars.values())
print(car.items())

car_copy = car.copy()
print(car_copy)
print(car.pop("model"))
print(car)


print("*"*50)
d = {"sfo":"San Francisco", "nyc":"New York"}
print(d)

d = {}
d["sfo"]="San Francisco"
d["nyc"]="New York"
print(d)



print("*"*50)


# d = new dict()
# d["sfo"]="San Francisco"
# d["nyc"]="New York"
# print(d)