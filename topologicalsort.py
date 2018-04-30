from collections import defaultdict

class TopologicalSort:
    def __init__(self, V=[], E=[]):
        '''
        DAG: Directed Acyclic Graph
        Edge is
        '''
        self.V = V
        self.E = defaultdict(list)

    def add_edge(self, edge):
        self.E[edge[0]].append(edge[1])

    def screen(self):
        print('vertices ',self.V)
        print('Edges ',self.E)

