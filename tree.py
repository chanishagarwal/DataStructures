class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


class Tree:
	def __init__(self):
		self.head = None

	def push(self, node):
		# For the top node/root node.
		if not self.head:
			self.head = node

		else:
			mh = self.head # MovingHead
			while(True):
				if node.data >= mh.data:
					if mh.right:
						mh = mh.right
					else:
						mh.right = node
						return True
				else:
					if mh.left:
						mh = mh.left
					else:
						mh.left = node
						return True

if __name__ == '__main__':
	tree = Tree()
	tree.push(Node(10))
	tree.push(Node(1))
	tree.push(Node(15))
	tree.push(Node(5))
	tree.push(Node(11))
	tree.push(Node(9))
	tree.push(Node(14))
	print(tree.head.data)
