from tree import Tree, Node
from preOrderTraversal import preorder

def even(n):
	if n%2 ==0:
		return True
	return False

def listtobst(t, l):
	'''
	t = Tree object
	l = input list
	'''
	if not l:
		return None 

	if even(len(l)):
		pos = int(len(l)/2) 
	else:
		pos = int((len(l)-1)/2) 

	v = l[pos]
	print(v)
	node = Node(v)
	left = l[:pos]
	right = l[pos+1:]
	t.push(node)
	if left:
		listtobst(t, left)
	if right:
		listtobst(t,right)
	return None

def run(inputlist):
	import ipdb;ipdb.set_trace()
	length = len(inputlist)
	t = Tree()
	listtobst(t, inputlist)
	# preorder(t.head)

if __name__ == '__main__':
	inputlist = [9,8,7,5,6,4,3,1,2,11]
	inputlist.sort()
	run(inputlist)
	

