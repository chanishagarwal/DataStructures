from tree import Tree, Node

def preorder(root):
	print(root.data)
	if root.left:
		preorder(root.left)
	if root.right:
		preorder(root.right)
	return None

def run(root):
	preorder(root)


if __name__ == '__main__':
	t = Tree()
	t.push(Node(5))
	t.push(Node(4))
	t.push(Node(3))
	t.push(Node(2))
	t.push(Node(9))
	t.push(Node(7))
	t.push(Node(11))
	run(t.head)


