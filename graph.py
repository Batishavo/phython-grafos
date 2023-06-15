class Graph:
    def __init__(self,nodes):
        self.nodes = nodes
        self.adj_list = {}
        for i in self.nodes:
            self.adj_list[i] =[]
    def add_edge(self,u,v):
        self.adj_list[u].append(v)
    def printGraph(self):
        for i,j in self.adj_list.items():
            print(i,"->",j)

graph = Graph([1,2,3,4,5,6,7])

graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(2,1)
graph.add_edge(2,4)
graph.add_edge(2,5)
graph.add_edge(3,7)
graph.printGraph()