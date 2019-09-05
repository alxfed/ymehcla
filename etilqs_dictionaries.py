"""
From the very beginning of sqlite3
"""

import sqlite3

conn = sqlite3.connect('/media/alxfed/toca/dbase/logbase.sqlite')

conn.row_factory = sqlite3.Row
cur = conn.cursor()

cur.execute("SELECT * FROM cars")
rows = cur.fetchall()
for row in rows:
    print(f"{row['id']} {row['name']} {row['price']}")

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()