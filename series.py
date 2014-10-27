# Series class

class Series(object):
    def __init__(self, name):
        self.id = 0
        self.name = name

    def getId(self):
        return self.id

    def getName(self):
        return self.name

        # Write the headers for the input series

    def writeHeader(self, cursor, runId):
        setSeries = 'INSERT INTO series(runId, name) VALUES(%s, %s) RETURNING id'
        cursor.execute(setSeries, (runId, self.getName()))
        (self.id,) = cursor.fetchone()



