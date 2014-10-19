#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('electricalframework.db')

c = conn.cursor()

c.execute('SELECT * FROM run')
print c.fetchone()

conn.commit

conn.close

