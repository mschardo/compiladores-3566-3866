class Queue:
	def __init__(self):
		self.list = []
	
	def empty(self):
		return len(self.list) == 0
	
	def put(self, item):
		self.list.append(item)
	
	def get(self):
		item = self.list[0]
		self.list = self.list[1:]
		return item