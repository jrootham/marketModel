name = 'Spot Market'

def auction(totalLoad, supplierList):
	localList = list(supplierList)

	required = totalLoad
	
	while required > 0 and len(localList) > 0:

		found = 0
		minimum = localList[0]

		for supplier in localList:
			if supplier.bid()['price'] <= minimum.bid()['price']:
				minimum = supplier

		
		allocated = min(required, minimum.bid()['volume'])
		required -= allocated
		minimum.price.setValue(minimum.bid()['price'])
		minimum.supply.setValue(allocated)

		localList.remove(minimum)



