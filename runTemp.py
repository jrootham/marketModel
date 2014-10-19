#!/usr/bin/python

import run

import load.heating
import supplier.gas
import market.spot
import inputs.temperature

Gas = supplier.gas.Gas
Temperature = inputs.temperature.Temperature
Heating = load.heating.Heating

inputList = [Temperature(19, -.5)]
loadList = [Heating(17, .5), Heating(18, 1)]
supplierList = [Gas(1, .07), Gas(10, .08)]
market = market.spot

run.run(inputList, loadList, supplierList, market)

