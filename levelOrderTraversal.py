from tree import Tree
from tree import Node
size = 100

def levelordertraversal(A, B):
	while(A): 
		r = A.pop(0)
		if r.data:
			print(r.data)
		if r.left:
			B.append(r.left)

		if r.right:
			B.append(r.right)

		if (not r.left) and (not r.right) and (not A):
			break
	if B:
		print('\n')
		levelordertraversal(B, A)
	return None

def run(root):
	import ipdb;ipdb.set_trace()
	A = []
	A.append(root)
	B = []
	levelordertraversal(A, B)







if __name__ == '__main__':
	tree = Tree()
	tree.push(Node(10))
	tree.push(Node(1))
	tree.push(Node(15))
	tree.push(Node(5))
	tree.push(Node(11))
	tree.push(Node(9))
	tree.push(Node(14))
	run(tree.head)
