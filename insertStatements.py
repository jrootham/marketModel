import sqlite3
conn = sqlite3.connect('electricalframework.db')

c = conn.cursor()

c.execute("INSERT INTO run ('id','name') VALUES (NULL,'david'),(NULL,'john'),(NULL,'parish'),(NULL,'gordon'),(NULL,'fife'),(NULL,'joshua')")

c.execute("INSERT INTO series ('id' ,'runId','name') VALUES (NULL,1,'bear'), (NULL,2,'zebra'), (NULL,3,'horse'), (NULL,4,'giraffe'), (NULL,5,'lion')")

c.execute("INSERT INTO point ('id', 'seriesId','sequence','value') VALUES  (NULL,1,2,3.5),(NULL,2,5,3.5),(NULL,3,7,9.5),(NULL,4,13,9.5),(NULL,5,20,9.5),(NULL,6,33,9.5),(NULL,7,53,9.5),(NULL,1,2,3.5),(NULL,2,5,3.5),(NULL,3,7,9.5),(NULL,4,13,9.5),(NULL,5,20,9.5)")


conn.commit()

#for row in c.execute('SELECT * FROM run'):
#        print row

#for row in c.execute('SELECT * FROM series'):
#        print row

#for row in c.execute('SELECT * FROM point'):
#        print row

conn.close()

