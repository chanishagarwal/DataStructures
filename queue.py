class Queue():
	def __init__(self):
		self.q = []

	def queue(self,value):
		self.q.append(value)

	def dqueue(self):
		if self.q:
			return self.q.pop(0)
		else:
			print('Queue is empty')

	def display(self):
		print(self.q)

	def is_empty(self):
		if self.q:
			return True
		return False


if __name__ == '__main__':
	s = Queue()
	[s.queue(i) for i in range(10)]
	s.display()
	print(s.dqueue())
	print(s.dqueue())
	s.queue(11)
	s.display()