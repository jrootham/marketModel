import series

class Heating(series.Series):
	def __init__(self, setPoint, consumption):
		super(Heating, self).__init__('Heating Load')
		self.setPoint = setPoint
		self.consumption = consumption

	def getValue(self, inputPoint):
		temp = inputPoint['temp']
		return max(0, (self.setPoint - temp)) * self.consumption 


