'''
BFS: Breadth First Search
This scripts provides bfs, level order traversal with depth of each node, Max height in O(n)
'''

from tree import Tree, Node
from queue import Queue


class BFS:
	def __init__(self, head):
		self.head = head

	def run(self):
		output = []
		q = Queue()
		node = self.head
		q.queue((node, 0))
		while(q.is_empty()):
			node, level = q.dqueue()
			if node.left:
				q.queue((node.left, level+1))
			if node.right:
				q.queue((node.right, level+1))

			output.append((node.data, level))

		return output

	def height(self):
		return (self.run()[-1][1])



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
	bfs = BFS(head)
	print(bfs.run())
	print(bfs.height())

