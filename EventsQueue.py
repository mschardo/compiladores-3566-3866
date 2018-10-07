class Event:
	def __init__(self, time, handler, task):
		self.time = time
		self.handler = handler
		self.task = task
		return

	def __str__(self):
		return str(self.__dict__)

	def __repr__(self):
		return str(self.__dict__)

	def __eq__(self, other): 
		return self.__dict__ == other.__dict__

class Node:
	def __init__(self, event):
		if isinstance(event, Event):
			self.event = event
			self.next = None
		else:
			print("Object is not of type Event.")
		return

	def __str__(self):
		return str(self.__dict__)

	def __repr__(self):
		return str(self.__dict__)

	def has_event(self, event):
		if self.event == event:
			return True
		else:
			return False

class DoubleLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		return

	def __repr__(self):
		return str(self.__dict__)

	def is_empty(self):
		if self.head is None:
			return True
		else:
			return False

	def length(self):
		count = 0
		current_node = self.head

		while current_node is not None:
			count += 1
			current_node = current_node.next
		return count

	def print_list(self):
		current_node = self.head

		while current_node is not None:
			print(current_node.event)
			current_node = current_node.next
		
		return

	def search(self, event):
		current_node = self.head
		node_id = 1
		results = []

		while current_node is not None:
			if current_node.has_event(event):
				results.append(node_id)

			current_node = current_node.next
			node_id += 1

		return results

	def add_event(self, item, position = None):
		if not isinstance(item, Node):
			print("Item is not of type Node.")
			return

		length = self.length()

		if position is None:
			position = length

		if position < 0:
			print("Negative position not valid.")
			return
		elif position > 0:
			if position > length:
				print("Invalid position %d for list of length %d" % (position, length))
				return

			else:
				current_position = 1
				current_node = self.head
				while current_node.next is not None and current_position != position:
					current_node = current_node.next
					current_position += 1

		if position == length:
			if self.is_empty():
				self.head = item
				item.next = None
				self.tail = item
			else:
				self.tail.next = item
				self.tail = item

		elif position == 0:
			item.next = self.head
			self.head = item

		else:
			item.next = current_node.next
			current_node.next = item

		return

	def add_in_time_order(self, item):
		if self.is_empty():
			self.add_event(item)
		else:
			if item.event.time > self.tail.event.time:
				self.add_event(item, self.length())
				return

			if item.event.time < self.head.event.time:
				self.add_event(item, 0)
				return

			position = 0
			current_node = self.head
			
			while current_node.next is not None and item.event.time > current_node.event.time:
				current_node = current_node.next
				position += 1

			self.add_event(item, position)

		return

	def remove_item_by_id(self, item_id):
		if item_id is None:
			return

		current_id = 1
		current_node = self.head
		previous_node = None
		to_delete = False

		while current_node is not None:
			next_node = current_node.next

			if isinstance(item_id, list):
				to_delete = current_id in item_id
			else:
				to_delete = current_id == item_id

			if to_delete:
				if previous_node is not None:
					previous_node.next = current_node.next
				else:
					self.head = current_node.next

			previous_node = current_node
			current_id += 1
			current_node = current_node.next
			to_delete = False

		return

	def remove_event(self, event):
		self.remove_item_by_id(self.search(event))
		return