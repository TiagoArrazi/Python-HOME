import matplotlib.pyplot as plt
import numpy as np

A = np.array([100,200,300,400,500,450,320,190,50])
B = np.array([200,400,600,800,1000,900,640,380,100])
C = np.array([150,300,450,600,750,675,480,285,75])

plt.plot(A, c = 'Red', marker = 'v', label = 'A')
plt.plot(B, c = 'Blue', marker = '^', label = 'B')
plt.plot(C, c = 'Black', ls = '--', marker = 'o', label = 'C')

plt.legend()

plt.show()


