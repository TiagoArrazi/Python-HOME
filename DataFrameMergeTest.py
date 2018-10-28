import pandas as pd
from db import DemoDB

database = DemoDB()

#print(database.tables)

album = database.tables.Album.all() #this variable receives the "Album" table from the database
artist = database.tables.Artist.all() #this variable receives the "Artist" table from the database

album_artist = pd.merge(artist, album) #merges both dataframes into a bigger one
