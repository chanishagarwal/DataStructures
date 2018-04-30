class MaxHeap:
	def __init__(self):
		self.data = []

	def insert(self, value):
		self.data.append(value)
		size = len(self.data)
		i = size - 1
		while(i>0):
			child = value
			if round((i-1)/2) >= 0:
				parent = self.data[round((i-1)/2)] if i>0 else None
			else:
				break

			if child > parent:
				self.data = swap(self.data, round((i-1)/2), i)
				i = round((i-1)/2)
			else:
				i -= 1
		print(self.data)


	def get_max(self):
		value = self.data.pop(0)
		self.data = heapify(self.data)
		print('max ', value)

	def get_list(self):
		print(self.data)


def heapify(unheapified):
	unheapified.insert(0,0)
	i = 1
	while(i<len(unheapified)):
		parent = unheapified[i]
		left = unheapified[2*i] if 2*i < len(unheapified) else None
		right = unheapified[2*i+1] if 2*i+1 < len(unheapified) else None

		if not left and not right:
			i += 1
			continue
		bigone, pos  = thebigone(left, right, i)
		if parent < bigone:
			unheapified = swap(unheapified, pos, i)
			i = pos
		else:
			i += 1
	unheapified.pop(0)
	print('heapified', unheapified)
	print('\n')
	return unheapified

def swap(inplist, posA, posB):
	elementA =inplist[posA]
	inplist[posA] = inplist[posB]
	inplist[posB] = elementA
	return inplist

def thebigone(a,b, i):
	if not a and b:
		return b, 2*i+1
	if a and not b:
		return a, 2*i

	if a>b:
		return a, 2*i
	if a<b:
		return b, 2*i+1

if __name__ == '__main__':
	inp = [12,3,4,5,1,2,9,8]
	mh = MaxHeap()
	mh.insert(12)
	mh.insert(3)
	mh.insert(4)
	mh.insert(5)
	mh.insert(1)
	mh.insert(2)
	mh.insert(9)
	mh.insert(8)
	mh.get_max()
	mh.get_list()
