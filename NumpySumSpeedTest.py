import numpy as np

a = 0

for i in range(1,100000001):
    a += i
print(a)

a = np.arange(1,100000001, dtype = 'int64').sum()
print(a)
