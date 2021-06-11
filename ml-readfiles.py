#Importando as bibliotecas:
import sqlite3 as sq3
import pandas.io.sql as pds
import pandas as pd

#Initialize path to SQLite database
path = "classic_rock.db"
con = sq3.Connection(path)

#Reading data:
#Write the query
query = '''
SELECT *
FROM rock_songs;
'''
#Execute the query:
observations = pds.read_sql(query,con)
observations.head()

#Write the query:
query = '''
SELECT Artist, Release_Year, COUNT(*) AS num_songs, AVG(PlayCount) AS avg_plays
    FROM rock_songs
    GROUP BY Artist, Release_Year
    ORDER BY num_songs desc;
    '''
#Execute the query:
observations = pds.read_sql(query,con)
observations.head()
