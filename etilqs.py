"""
From the very beginning of sqlite3
"""

import sqlite3

conn = sqlite3.connect('/media/alxfed/toca/dbase/logbase.sqlite')
cur = conn.cursor()

cur.execute('''create table companies
            (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
cur.execute("insert into companies values ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()