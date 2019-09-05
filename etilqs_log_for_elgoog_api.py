"""
From the very beginning of sqlite3
"""
import sqlite3
import itertools
import googlemaps
from os import environ

def RequestCompanyList(names_list):
    connb = sqlite3.connect('/media/alxfed/toca/dbase/firstbase.sqlite')
    cursb = connb.cursor()
    cursb.execute("select Name from companies")
    tuples = cursb.fetchall()
    for tuple in tuples
        name, = tuple
        if name.endswith('Llc') or name.endswith('Inc')
    names_list = list(itertools.chain(*tuples))
    connb.close()


names_list = list()
# Name and schema of today's log, change before the run!
sql = '''CREATE TABLE log_september_4
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
r = sqlite3.enable_callback_tracebacks(True)
cur = conn.cursor()
cur.execute(sql)

# main cycle begins here

values = ('2006-01-05','BUY','RHAT',100,35.14)

# Insert a row of data into the log table
cur.execute("insert into log_september_4 values (?, ?, ?, ?, ?)", values)
conn.commit()

# main cycle ends here

# close the connection
conn.close()

print('ok')