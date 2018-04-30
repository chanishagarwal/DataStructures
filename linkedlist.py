class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, node):
		if self.head is None:
			self.head = node
		else:
			temp = self.head
			node.next = temp
			self.head = node

	def stackpop(self):
		a = self.head
		if a.next:
			print(a.data)
			self.head = a.next
			return a.data
		else:
			self.head = None
			print(a.data)
			print('stack empty')
			return a.data

	def queuepop(self):
		if self.head:
			if self.head.next is None:
				popdata = self.head.data
				print(popdata)
				self.head = None
				print('Empty now')
				return popdata
			else:
				movinghead = self.head
				while(movinghead.next.next != None):
					movinghead = movinghead.next

				temp = movinghead.next
				movinghead.next = None
				print(temp.data)
				return (temp.data)

	def display(self):
		movinghead = self.head
		while(movinghead.next != None):
			print(movinghead.data)
			movinghead = movinghead.next
		print(movinghead.data)


if __name__ == '__main__':
	ll = LinkedList()
	ll.push(Node(1))
	ll.push(Node(2))
	ll.push(Node(3))
	ll.push(Node(4))
	ll.push(Node(5))
	ll.stackpop()
	ll.queuepop()
	ll.push(Node(6))
	ll.queuepop()
	print('\n')
	ll.display()


