from queue import Queue
eventQueue = SimpleQueue()
eventsDone = SimpleQueue()


class Event:
	def __init__(self, time, handler, task):
		self.time = time
		self.handler = handler
		self.task = task
		self.done = False
		
	def done(self):
		self.done = True


def main():
	# Add initial events and set tick
	while not eventQueue.empty():
		eventQueue.get(False)
	eventQueue.put(Event(1, 'EVENT_1', "Task 1"))
	eventQueue.put(Event(2, 'EVENT_2', "Task 2"))
	eventQueue.put(Event(3, 'EVENT_3', "Task 3"))
	eventQueue.put(Event(4, 'EVENT_4', "Task 4"))
	tick = 0

	# Handle the events
	while True:
		if eventQueue.empty():
			break
		event = eventQueue.get(False)
		if event is None:
			break
		tick = event.time
		if event.type == 'EVENT_1':
			treat_event_1()
		elif event.type == 'EVENT_2':
			treat_event_2()
		elif event.type == 'EVENT_3':
			treat_event_3()
		elif event.type == 'EVENT_4':
			treat_event_4()
		

if __name__ == "__main__":
	main()