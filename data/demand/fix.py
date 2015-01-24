#!/usr/bin/python

__author__ = 'jrootham'

months = \
    {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06',
     'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

def fixLine(year, line):
    list = line.split(',', 1)
    pieces = list[0].split('-')
    list[0] = year + '/' + months[pieces[1]] + '/' + pieces[0]
    return ','.join(list)

for year in range(2003, 2010):
    inName = 'ZonalDemands_' + str(year) + '.csv'
    outName = 'fixed' + str(year) + '.csv'

    with open(inName) as inFile:
        first = True
        with open(outName, 'w') as outFile:
            for line in inFile:
                if (first):
                    outFile.write(line)
                    first = False
                else:
                    outFile.write(fixLine(str(year), line))


