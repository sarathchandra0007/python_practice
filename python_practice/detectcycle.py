from collections import defaultdict
class Graph(object):
    def __init__(self,v):
        self.graph=defaultdict(list)
        self.v=v
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def isCyclic(self):
        visited=[False]*self.v
        recstack=[False]*self.v

        for i in range(self.v):
            if visited[i]==False:
                if self.checkcycle(i,visited,recstack)==True:
                    return True

        return False
    def checkcycle(self,i,visited,recstack):
        visited[i]=True
        recstack[i]=True

        for n in self.graph[i]:
            if visited[n]==False:
                if self.checkcycle(n,visited,recstack)==True:
                    return True
                else:
                    recstack[n]==True
                    return True
        return False
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
if g.isCyclic() == 1:
    print ("Graph has a cycle")
else:
    print ("Graph has no cycle")
