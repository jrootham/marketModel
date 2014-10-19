import series

class Value(series.Series):
	def __init__(self, name):
		super(Value, self).__init__(name)
		self.current = 0

	def getValue(self):
		return self.current

	def setValue(self, value):
		self.current = value



