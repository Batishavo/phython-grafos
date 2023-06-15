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
    def DFSRec(self,source,visited):
        visited.add(source)
        print(source)
        for i in self.adj_list[source]:
            if i not in visited:
                self.DFSRec(i,visited)
    def DFS(self,source):
        visited=set()
        self.DFSRec(source,visited)


graph = Graph([1,2,3,4])

graph.add_edge(1,2)
graph.add_edge(1,4)
graph.add_edge(2,1)
graph.add_edge(2,3)
graph.add_edge(3,2)
graph.add_edge(3,4)
graph.add_edge(4,1)
graph.add_edge(4,3)
graph.printGraph()
graph.DFS(1)