#!/usr/bin/python

# Create new database

import sqlite3
conn = sqlite3.connect('electricalframework.db')

c = conn.cursor()

run = 'CREATE TABLE run ('
run += 'id INTEGER PRIMARY KEY AUTOINCREMENT,'
run += 'name CHAR(50))'

c.execute(run)

series = 'CREATE TABLE series ('
series += 'id INTEGER PRIMARY KEY AUTOINCREMENT,'
series += 'runId INT,'
series += 'name CHAR(50))'

c.execute(series)

point = 'CREATE TABLE point ('
point += 'id INTEGER PRIMARY KEY AUTOINCREMENT,'
point += 'seriesId INT,'
point += 'sequence INT,'
point += 'value NUM)'

c.execute(point)

# Save (commit) the changes
conn.commit()
