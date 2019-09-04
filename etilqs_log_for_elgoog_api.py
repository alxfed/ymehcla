"""
From the very beginning of sqlite3
"""
import sqlite3
import pandas as pd
import googlemaps
from os import environ

# Initial data
file_path = '/media/alxfed/toca/aa-crm/companies.csv'
companies = pd.read_csv(file_path, dtype='str')
company_names = companies['Name']
names = company_names.values
print('ok')


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