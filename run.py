#  run 
import sqlite3
import sys

#  Write the headers for a series

def seriesHeaders(c, runId, seriesList):
	for series in seriesList:
		series.writeHeader(c, runId)

#  Write the input values into the database
		
def inputValues(c, inputList, step):
	for inputThing in inputList:
		setPoint = 'INSERT INTO point(seriesId, sequence, value) VALUES(?, ?, ?)'
		c.execute(setPoint, (inputThing.getId(), step, inputThing.getValue(step)))

# write the load values into the database

def loadValues(c, loadList, step, inputPoint):
	for load in loadList:
		setPoint = 'INSERT INTO point(seriesId, sequence, value) VALUES(?, ?, ?)'
		c.execute(setPoint, (load.getId(), step, load.getValue(inputPoint)))
		
# write the supplier values into the database

def supplierValues(c, supplierList, step):
	for supplier in supplierList:
		setPoint = 'INSERT INTO point(seriesId, sequence, value) VALUES(?, ?, ?)'
		c.execute(setPoint, (supplier.price.getId(), step, supplier.price.getValue()))
		c.execute(setPoint, (supplier.supply.getId(), step, supplier.supply.getValue()))
		
# create an input data structure for a given sequence point

def makePoint(inputList, step):
	return {inputThing.getSymbol(): inputThing.getValue(step) for inputThing in inputList}

# run the model, fill in the database

def run(inputList, loadList, supplierList, market):
	conn = sqlite3.connect('electricalframework.db')

	c = conn.cursor()

	if len(sys.argv) > 2:
		name = sys.argv[1]
		stepCount = int(sys.argv[2])
		setname = 'INSERT INTO run (name) VALUES(?);'
		c.execute(setname, (name,))

		c.execute('SELECT last_insert_rowid() FROM run')
		(runId,) = c.fetchone()

		seriesHeaders(c, runId, inputList)
		seriesHeaders(c, runId, loadList)
		for supplier in supplierList:
			supplier.price.writeHeader(c, runId)
			supplier.supply.writeHeader(c, runId)

		conn.commit()

		for step in range(stepCount):
			inputValues(c, inputList, step)
			inputPoint = makePoint(inputList, step)
			loadValues(c, loadList, step, inputPoint)

			totalLoad = 0
			for load in loadList:
				totalLoad += load.getValue(inputPoint)

			market.auction(totalLoad, supplierList)
 		
			supplierValues(c, supplierList, step)

			conn.commit()
	else:
		print ('Usage: ./runScript.py name stepCount')


