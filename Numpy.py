import numpy as np

A = np.array([[10,20,30],[40,50,60],[70,80,90]])

print('Numpy array A')
print(A)
print('\n')

print('Amount of dimensions of A')
print(A.ndim)
print('\n')

print('The transposed array of A')
print(A.transpose())
print('\n')

print('The diagonal of array A')
print(A.diagonal())
print('\n')

#-------------------------------------------------------

M1 = np.array([[1,2],[3,4],[5,6]])
M2 = np.array([[7,8],[9,10],[11,12]])

print('M1')
print(M1)
print('\n')

print('M2')
print(M2)
print('\n')

print('M1 + M2 element-wise')
print(M1 + M2)
print('\n')

print('M1 * M2 element-wise')
print(M1 * M2)
print('\n')

#------------------------------------------------------

M3 = np.array([1,2,3,4,5,6,7,8,9])

print('M3')
print(M3)
print('\n')

print('The sum of all elements in M3')
print(M3.sum())
print('\n')

print('The index of the highest value in M3')
print(M3.argmax())
print('\n')

print('The index of the lowest value in M3')
print(M3.argmin())
print('\n')

print('The mean value of M3')
print(M3.mean())
print('\n')


