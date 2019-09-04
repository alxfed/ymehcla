"""
From the very beginning of sqlite3
"""
import sqlite3
import googlemaps
from os import environ

# Name and schema of today's log, change before the run!
sql = '''CREATE TABLE log_today
            (
                date text, 
                trans text, 
                symbol text, 
                qty real, 
                price real
            )
'''
# Open connection and create a table
conn = sqlite3.connect('/media/alxfed/toca/dbase/logbase.sqlite')
cur = conn.cursor()
cur.execute(sql)

# main cycle begins here

values = ('2006-01-05','BUY','RHAT',100,35.14)

# Insert a row of data into the log table
cur.execute("insert into log_today values (?, ?, ?, ?, ?)", values)
conn.commit()

# main cycle ends here

# close the connection
conn.close()

print('ok')