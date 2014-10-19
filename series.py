# Series class

class Series(object):
	def __init__(self, name):
		self.id = 0
		self.name = name

	def getId(self):
		return self.id

	def getName(self):
		return self.name

#  Write the headers for the input series

	def writeHeader(self, c, runId):
		setSeries = 'INSERT INTO series(runId, name) VALUES(?, ?)'
		c.execute(setSeries, (runId, self.getName()))
		c.execute('SELECT last_insert_rowid() FROM series')
		(self.id,) = c.fetchone()



