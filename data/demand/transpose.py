#!/usr/bin/python

import regions

__author__ = 'jrootham'

import psycopg2

connect = psycopg2.connect('dbname=market')
readCursor = connect.cursor()
writeCursor = connect.cursor()

readCursor.execute('SELECT * FROM rawdemand')
rowList = readCursor.fetchall()

for row in rowList:
    day = row[0]
    hour = row[1]

    for zone in regions.zoneList:
        demand = row[zone + 1]

        writeCursor.execute('INSERT INTO demand (the_day, the_hour, the_zone, demand) VALUES(%s, %s, %s, %s)',
                            (day, hour, zone, demand))

connect.commit()

readCursor.close()
writeCursor.close()

connect.close()

