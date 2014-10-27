#!/usr/bin/python

import psycopg2

connect = psycopg2.connect('dbname=market')
cursor = connect.cursor()

cursor.execute('SELECT * FROM run')
print cursor.fetchone()

cursor.close
connect.close

