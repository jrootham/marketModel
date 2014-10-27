import series


class Simple(series.Series):
    def __init__(self):
        super(Simple, self).__init__('Simple Inputs')

    def getValue(self, sequence):
        return .5

    def getSymbol(self):
        return 'si'

