import math as m

double = lambda x: x * 2
triple = lambda x: x * 3
square = lambda x: x ** 2
cube = lambda x: x ** 3
sqRoot = lambda x: m.sqrt(x)

print(double(4))
print(triple(4))
print(square(4))
print(cube(4))
print(sqRoot(4))

l = [1,2,3,4,5,6,7,8,9,10]

print(list(filter(lambda x: x % 2 == 0, l)))
print(list(map(lambda x: x * 2, l)))
