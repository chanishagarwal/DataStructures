from tree import Tree, Node
from stack import Stack
from copy import deepcopy


class RTL:
	'''
	Root To Leaf
	All the Paths from root node to leaf node
	Will also calculate all the possible sum value from root to leaf path
	'''
	def __init__(self, head):
		self.head = head

	def all_paths(self):
		movinghead = self.head
		smallstack = Stack(100) #size
		smallstack.push((movinghead, [movinghead.data]))
		# print(smallstack.display())
		paths_stack = Stack(100)
		while(not smallstack.is_empty()):
			node, l = smallstack.pop()
			left = deepcopy(l)
			right = deepcopy(l)
			# print(node,l)
			if node.left:
				left.append(node.left.data)
				smallstack.push((node.left, left)) 
			if node.right:
				right.append(node.right.data)
				smallstack.push((node.right, right))

			if (not node.left) and (not node.right):
				paths_stack.push(l)

		return self.display_all_paths(paths_stack)

	def display_all_paths(self, st):
		output = []
		while(not st.is_empty()):
			output.append(st.pop())
		return output

	def root_to_leaf_sum(self):
		paths = self.all_paths()
		output = [sum(each) for each in paths]
		return output




if __name__ == '__main__':
	tree = Tree()
	tree.push(Node(10))
	tree.push(Node(1))
	tree.push(Node(15))
	tree.push(Node(5))
	tree.push(Node(11))
	tree.push(Node(9))
	tree.push(Node(20))
	tree.push(Node(45))
	tree.push(Node(4))
	tree.push(Node(13))
	tree.push(Node(14))
	head = tree.head
	rtl = RTL(head)
	print('paths ',rtl.all_paths())
	print('sum list', rtl.root_to_leaf_sum())