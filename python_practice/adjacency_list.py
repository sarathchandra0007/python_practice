class Vertex(object):
    def __init__(self,vid):
        self.vid=vid
        self.connectedTo={}
    def addneighbour(self,nbr,weight=0):
        self.connectedTo[nbr]=weight
    def getconnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.vid
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
    def __str__(self):
        return str(self.vid) + " is connected to" + str([x for x in self.connectedTo])

class Graph(object):
    def __init__(self):
        self.vertices={}
        self.noofvertices=0
    def addVertex(self,key):
        self.noofvertices+=1
        ver=Vertex(key)
        self.vertices[key]=ver
        print (self.vertices)
        return ver



g=Graph()
print (g.addVertex(1))

"""
v=Vertex(1)
#v=Vertex(v2)
#v=Vertex(v3)
v.addneighbour(2,5)
v.addneighbour(3,6)

print (str(v))
"""
