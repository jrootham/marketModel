import psycopg2
import numpy as np
import pandas
from pandas import DataFrame, Series


connect = psycopg2.connect('dbname=market')
cursor = connect.cursor()

cursor.execute('select * from run')
rows = cursor.fetchall()

cursor.description
df = DataFrame(rows, columns=zip(*cursor.description)[0])

import matplotlib.pyplot as plt

plt.scatter(df.symbol, df.services,
            marker='o',
            edgecolor='b',
            facecolor='none',
            alpha=0.5)
plt.xlabel('symbol')
plt.ylabel('services')
plt.savefig('alcohol_v_tobacco.png', fmt='png', dpi=100)
