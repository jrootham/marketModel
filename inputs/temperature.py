import series


class Temperature(series.Series):
    def __init__(self, start, increment):
        super(Temperature, self).__init__('Temperature')
        self.start = start
        self.increment = increment

    def getValue(self, step):
        return self.start + self.increment * step

    def getSymbol(self):
        return 'temp'

