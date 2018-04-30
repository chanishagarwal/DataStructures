from collections import defaultdict

class Graph:
    def __init__(self, vertices, edges):
    	'''
    	adjecency list represent dict 
    	keys are graph vertices/nodes
    	values are list which represents connected vertices.
    	{
			'verticeA': [(verticeB, Weight ,visited)]
			'verticeB': [(verticeC, Weight, visited), (verticeA, Weight, visited)]
    	}
    	'''
    	self.adjecency_list = defaultdict(list)
    	if len(edges[0]) == 3:
	        [self.adjecency_list[u].append((v, w, 0)) for u,v, w in edges]
	    else:
        	[self.adjecency_list[u].append((v, 0, 0)) for u,v in edges]

    def addEdge(self, edge):
    	'''
    	need to check if weight is present or not
    	'''
    	if len(edge) == 3:
    		self.adjecency_list[edge[0]].append((edge[1],edge[2],0)
    	else:
    		self.adjecency_list[edge[0]].append((edge[1],0,0)


if __name__ == '__main__':
    g = Graph(['a','b','c','d'], [('a','b'), ('b','c'), ('c','a'), ('d','c')])
    print(g.adjecency_list)