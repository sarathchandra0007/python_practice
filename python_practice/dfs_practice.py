from collections import defaultdict
class Graph(object):
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def DFS(self,start):
        visited=[False]*len(self.graph)
        self.DFSUtil(visited,start)
    def DFSUtil(self,visited,start):
        count=0
        visited[start]=True
        print (start,end=" ")
        for i in self.graph[start]:
            if visited[i]==False:
                self.DFSUtil(visited,i)
            else:
                count+=1
        print (count)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is Breadth First Traversal"
                           " (starting from vertex 2)")
g.DFS(2)
