from db import DB

database = DB(filename = 'logs.sqlite3', dbtype = 'sqlite')

log_df = database.query('select * from log where user_id = 3')
print(log_df)


