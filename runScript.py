#!/usr/bin/python

import run

import load.simple
import supplier.simple
import market.simple
import inputs.simple

inputList = [inputs.simple.Simple()]
loadList = [load.simple.Simple()]
supplierList = [supplier.simple.Simple()]
market = market.simple

run.run(inputList, loadList, supplierList, market)

