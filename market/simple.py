name = 'Simple Market'


def auction(totalLoad, supplierList):
    allocated = totalLoad / len(supplierList)

    for supplier in supplierList:
        supplier.price.setValue(.08)
        supplier.supply.setValue(allocated)


