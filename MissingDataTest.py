import pandas as pd
import numpy as np

data = {
	'Names' : ['John', 'Mary', 'Joseph', np.nan, 'Peter', 'James', 'Rose'],
	'Gender' : ['M', 'F', 'M', np.nan, 'M', 'M', np.nan],
	'Age' : [19, 20, np.nan, np.nan, 21, 18, 22],
	'Grade' : [4, 10, 7, np.nan, 8, 9, 7]
}

df = pd.DataFrame(data)
print(df)
print('\n')

#All of the modifications made in the DataFrame are not valid until the parameter "inplace = True" is provided to the DataFrame missing data correction methods, in instance df.dropna(inplace = True)

#------Removing Missing Data Techniques--------

print(df.dropna()) #disconsiders partially or totally incomplete rows
print('\n')

print(df.dropna(how = 'all')) #disconsiders totally incomplete rows only (axis = 0)
print('\n')

df['Graduation'] = np.nan #creating a new blank column

print(df)
print('\n')

print(df.dropna(how = 'all', axis = 1)) #disconsiders totally incomplete columns only (axis = 1)
print('\n')

print(df.dropna(thresh = 3)) #establishes a threshold of missing data, in instance, this line will remove only the row that misses 3 or more data, in this case row 3
print('\n')


#------Replacing Missing Data Techniques--------

print(df.fillna('Not informed')) #replaces every missing data with "Not informed"
print('\n')

#df['Age'].fillna(df['Age'].mean(), inplace = True) 
#replaces every missing data in the "Age" column with the mean of all the ages in the DataFrame permanently

#print(df)


#------Filtering Missing Data--------

print(df[df['Names'].notnull() & df['Age'].notnull()]) #shows the rows that don't contain any null data in the columns "Names" and "Age"

