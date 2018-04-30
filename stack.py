#Usually stack has size limitation because Earlier in C language we use to use Arrays, and arrays are of fixed length
# List has no such constraints so our Stack size could be anything
# Above code can be modifed based on that
#TODO: add is_empty field

class Stack():
	def __init__(self, size):
		self.size = size
		self.top = -1
		self.arr = []

	def push(self,value):
		if self.top == self.size -1:
			print('stack is full')
		else:
			self.arr.append(value)
			self.top += 1
		return None
		
	def pop(self):
		if self.top != -1:
			self.top -=1
			return(self.arr.pop())
		else:
			print('stack is empty')
			return None

	def is_empty(self):
		if self.top == -1:
			return True
		return False

	def display(self):
		return self.arr


if __name__ == '__main__':
	s = Stack(5)
	[s.push(i) for i in range(10)]
	s.pop()
	s.pop()
	s.push(11)
	s.display()