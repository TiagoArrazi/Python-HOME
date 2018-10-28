import pandas as pd
import numpy as np 

data = pd.read_csv('primary-results.csv')

#print(data['candidate'].unique()) #each unique value "candidate" can have

#print(pd.pivot_table(data, index = ['state', 'party', 'candidate'], values = ['votes'], aggfunc = {'votes' : np.sum}))

data['rank'] = data.groupby(['county', 'party'])['votes'].rank(ascending = False)

#print(data[data['county'] == 'Los Angeles'])

data_groupby = data.groupby(['state', 'party', 'candidate']).sum()
del data_groupby['fips']
del data_groupby['fraction_votes']
data_groupby.reset_index(inplace = True)
#print(data_groupby)

print(pd.pivot_table(data_groupby, index = ['state', 'party', 'candidate'], values = ['rank', 'votes']))

print(data_groupby[data_groupby['rank'] == 1]['candidate'].value_counts())




















