import pandas as pd

data = pd.read_csv('Copacabana_CSVReaderTest.csv', delimiter=';')

with pd.option_context('display.max_rows', 1000, 'display.max_columns', 17):
	print(data['Quartos'] > 5)
	print(data.loc[data['Quartos'] == 6])
	print(data.loc[data['Quartos'] == 5])
	print(data.loc[data['Quartos'] == 4])
	print(data.loc[data['DistFavela'] > 700 & data['DistPraia'] < 150])


