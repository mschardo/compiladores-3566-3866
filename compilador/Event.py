class Event:
	def __init__(self, type='', parameters={}, engine=''):
		self.type = type
		self.parameters = parameters
		self.engine = engine