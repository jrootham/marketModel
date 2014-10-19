import sqlite3
import numpy as np
import pandas
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import sys

#prepare system arguments
seriesId = sys.argv[1]

# get user to select series for display
#getRunID = input('please enter seriesID to display series/n')


con = sqlite3.connect('electricalframework.db')
cursor = con.execute('select * from point WHERE seriesId=%s' % seriesId)
rows = cursor.fetchall()

#test print
#print rows

df = DataFrame(rows, columns=zip(*cursor.description)[0])


plt.plot( df.value, df.sequence)
plt.xlabel('sequence')
plt.ylabel('value')
plt.savefig('framework.png', fmt='png', dpi=100)
plt.show()
