from collections import defaultdict
class graph(object):
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def DFS(self,index):
        visited=[False]*len(self.graph)
        self.dfsrec(visited,index)
    def dfsrec(self,visited,index):
        visited[index]=True
        print (index,end=" ")
        for i in self.graph[index]:
            if visited[i]==False:
                self.dfsrec(visited,i)


g=graph()                                               
g.addEdge(0, 1)                                         
g.addEdge(0, 2)                                         
g.addEdge(1, 2)                                         
g.addEdge(2, 0)                                         
g.addEdge(2, 3)                                         
g.addEdge(3, 3)                                         
g.DFS(2)                                                  
