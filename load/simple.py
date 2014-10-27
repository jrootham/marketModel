import series


class Simple(series.Series):
    def __init__(self):
        super(Simple, self).__init__('Simple Load')

    def getValue(self, inputPoint):
        return 1.6



