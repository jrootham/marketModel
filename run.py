# run
import psycopg2
import sys

#  Write the headers for a series

def seriesHeaders(cursor, runId, seriesList):
    for series in seriesList:
        series.writeHeader(cursor, runId)


#  Write the input values into the database

def inputValues(cursor, inputList, step):
    for inputThing in inputList:
        setPoint = 'INSERT INTO point(seriesId, sequence, value) VALUES(%s, %s, %s)'
        cursor.execute(setPoint, (inputThing.getId(), step, inputThing.getValue(step)))


# write the load values into the database

def loadValues(cursor, loadList, step, inputPoint):
    for load in loadList:
        setPoint = 'INSERT INTO point(seriesId, sequence, value) VALUES(%s, %s, %s)'
        cursor.execute(setPoint, (load.getId(), step, load.getValue(inputPoint)))


# write the supplier values into the database

def supplierValues(cursor, supplierList, step):
    for supplier in supplierList:
        setPoint = 'INSERT INTO point(seriesId, sequence, value) VALUES(%s, %s, %s)'
        cursor.execute(setPoint, (supplier.price.getId(), step, supplier.price.getValue()))
        cursor.execute(setPoint, (supplier.supply.getId(), step, supplier.supply.getValue()))


# create an input data structure for a given sequence point

def makePoint(inputList, step):
    return {inputThing.getSymbol(): inputThing.getValue(step) for inputThing in inputList}


# run the model, fill in the database

def run(inputList, loadList, supplierList, market):
    connect = psycopg2.connect('dbname=market')
    cursor = connect.cursor()

    if len(sys.argv) > 2:
        name = sys.argv[1]
        stepCount = int(sys.argv[2])
        setname = 'INSERT INTO run (name) VALUES(%s) RETURNING id;'
        cursor.execute(setname, (name,))
        (runId,) = cursor.fetchone()

        seriesHeaders(cursor, runId, inputList)
        seriesHeaders(cursor, runId, loadList)
        for supplier in supplierList:
            supplier.price.writeHeader(cursor, runId)
            supplier.supply.writeHeader(cursor, runId)

        connect.commit()

        for step in range(stepCount):
            inputValues(cursor, inputList, step)
            inputPoint = makePoint(inputList, step)
            loadValues(cursor, loadList, step, inputPoint)

            totalLoad = 0
            for load in loadList:
                totalLoad += load.getValue(inputPoint)

            market.auction(totalLoad, supplierList)

            supplierValues(cursor, supplierList, step)

            connect.commit()
    else:
        print ('Usage: ./runScript.py name stepCount')


