import pandas as pd
from db import DB

database = DB(filename = 'logs.sqlite3', dbtype = 'sqlite')

log_df = database.tables.log.all() #this variable receives the table "log"

log_df['date'] = pd.to_datetime(log_df['date'], format = '%Y-%m-%d %H:%M:%S.%f') #changing the date format to Python's datetime format

log_df.set_index(log_df['date'], inplace = True) #the column "date" is the new index of the DataFrame

print(log_df['2017']) #shows all the values that contain the 2017 in its date

print(log_df['2017-01-03 10:47:00' : '2017-01-03 10:51:00']) #ranged search
