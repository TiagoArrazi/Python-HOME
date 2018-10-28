import pandas as pd

S = pd.Series([1,2,-3,4,5,5])
T = pd.Series([7,-8,9])

print(S)
print(T)

print(S.describe())
print(T.describe())

print(S.duplicated())
print(T.duplicated())

print(S.abs())
print(T.abs())
