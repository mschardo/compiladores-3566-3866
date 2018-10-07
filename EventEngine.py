import sys
import EventsQueue as ev
from queue import Queue

eventList = ev.DoubleLinkedList()
tick = 0

def initialize_program(file_name):
	# Read file
	file = open(file_name, "r")
	file_lines = file.readlines()
	return file_lines

	# Empt queue
	while not eventList.empty():
		eventList.get(False)

	# Add initial events
	eventList.add_in_time_order(Node(Event(1, 'EVENT_1', "Task 1")))
	eventList.add_in_time_order(Node(Event(2, 'EVENT_2', "Task 2")))
	eventList.add_in_time_order(Node(Event(3, 'EVENT_3', "Task 3")))
	eventList.add_in_time_order(Node(Event(4, 'EVENT_4', "Task 4")))

	# Sets tick to 0
	tick = 0


def main(file_name):
	initialize_program(file_name)
events_list
	# Handle the events
	while True:
		if eventList.empty():
			break
		event = eventList.get(False)
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
	file_name = sys.argv[1]
	main(file_name)