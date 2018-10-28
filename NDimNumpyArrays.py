
import numpy as np

a = np.array(123) #0 dimensional array
b = np.array([1,2,3]) #1 dimensional array
c = np.array([[1,2,3],[4,5,6]]) #2 dimensional array
d = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]]) #3 dimensional array
e = np.array([[[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]],[[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]]]) #4 dimensional array

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print(e.ndim)            
