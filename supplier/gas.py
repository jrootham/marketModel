import value


class Gas:
    def __init__(self, bidVolume, bidPrice):
        self.price = value.Value('Gas Supplier - Price')
        self.supply = value.Value('Gas Supplier - Supply')

        self.bidVolume = bidVolume
        self.bidPrice = bidPrice

    def bid(self):
        return {'volume': self.bidVolume, 'price': self.bidPrice}

