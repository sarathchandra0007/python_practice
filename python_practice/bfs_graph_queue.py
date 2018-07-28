from collections import defaultdict
class graph(object):
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def BFS(self,index):
        queue=[]
        #print (len(self.graph))
        visited=[False]*len(self.graph)
        visited[index]=True
        queue.append(index)

        while queue:
            #print (queue1)
            s=queue.pop(0)
            print (s,end=" ")
            for i in self.graph[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True


g=graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is Breadth First Traversal"
                           " (starting from vertex 2)")
g.BFS(2)
