__author__ = 'jrootham'

import sys
import csv
import time
import psycopg2
import requests
import regions

URL = 'http://climate.weather.gc.ca/climateData/bulkdata_e.html'

def main():
    doRegions = []

    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            doRegions.append(int(arg))
    else:
        doRegions = range(1, len(regions.regionList) + 1)

    connect = psycopg2.connect('dbname=market')
    writeCursor = connect.cursor()

    then = time.time()
    fillRegions(writeCursor, doRegions)
    connect.commit()
    print (time.time() - then)

def fillRegions(writeCursor, doRegions):
    for regionRow in regions.regionList:
        zone, name, city, stationName, stationId, lat, long = regionRow

        if zone in doRegions:
            print name

            year = 2003
            for month in range(5,13):
                fillTemperature(writeCursor, zone, stationId, year, month, lat, long)

            for year in range(2004, 2014):
                for month in range(1,13):
                    fillTemperature(writeCursor, zone, stationId, year, month, lat, long)

def fillTemperature(writeCursor, zone, stationId, year, month, lat, long):
    options = {
        'format': 'csv',
        'stationID' : stationId,
        'Year': year,
        'Month': month,
        'Day': 1,
        'timeframe': 1,
        'submit': 'Download Data'
    }

    result = requests.get(URL, params=options)
    reader = csv.reader(result.iter_lines())

    latitude = 0
    longitude = 0

    count = 0

    header = True

    for row in reader:
        if header:
            if len(row) > 0:
                if (row[0] == 'Longitude'):
                    longitude = float(row[1])
                if (row[0] == 'Latitude'):
                    latitude = float(row[1])
                if (row[0] == 'Date/Time'):
                    header = False

                    if longitude != long or latitude != lat:
                        print(stationId, year, month, "failed")
                        return
        else:
            if (len(row) > 7 and row[6] != ''):
                count += 1
                day = row[0][:10]
                hour = int(row[0][11:13]) + 1
                temperature = float(row[6])
                save(writeCursor, zone, day, hour, temperature)

    print zone, year, month, count


def save(writeCursor, region, day, hour, temperature):
    sql = "UPDATE demand SET temperature=%s WHERE the_zone=%s AND the_day=%s AND the_hour=%s;"
    writeCursor.execute(sql, (temperature, region, day, hour))

