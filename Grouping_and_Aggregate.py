import pandas as pd
import numpy as np

df = pd.read_csv('primary-results.csv')

with pd.option_context('display.max_rows', 1000, 'display.max_columns', 10):
	
	#print(df)

	#print(df.groupby('candidate').aggregate({'votes' : [min, np.mean, max]})) #shows the 		     		minimum, the maximum and the average amount of votes each candidate got in each state

	#print(df[df['votes'] == 590502]) #shows the row in which Hillary Clinton according to the dataset, had 		the total amount of votes of exactly 590502
	
	#print(df.groupby('candidate').aggregate({'fraction_votes' : [min, np.mean, max]})) #shows the 		 		minimum, the maximum and the average fraction of votes each candidate got in each state

	
	#shows the rows in which the candidates got 100% of the votes

	#print(df[(df['fraction_votes'] == 1) & (df['candidate'] == 'Hillary Clinton')]) 
	#print(df[(df['fraction_votes'] >= 0.9) & (df['candidate'] == 'Donald Trump')])
	#print(df[(df['fraction_votes'] == 1) & (df['candidate'] == 'Bernie Sanders')])


	#shows the rows in which the sum of the amount of votes per state is bigger than 1,000,000 

	def votes_filter(x):
		return x['votes'].sum() > 1000000

	#print(df.groupby('state').filter(votes_filter))


	#shows the amount of votes each candidate got in each state	

	print(df.groupby(['state_abbreviation', 'candidate'])['votes'].sum())

	

	
