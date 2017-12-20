class Vertex:

    def __init__(self, name):
        self.name = name
        self.data = None
        self.edges = {}

    def getName(self):
        return self.name

    def getData(self):
        return self.data

    def getEdges(self):
        return edges

    def setName(self, newname):
        self.name = newname

    def setData(self, newdata):
        self.data = newdata

    #connecting = name of the node connecting to
    def addEdge(self, connecting, weight):
        self.edges[connecting] = weight

    def getWeight(self, connected):
        if connected in self.edges.keys():
            return self.edges[connected]
        return 0

    def __str__(self):
        return(str(self.name) + ":\t" + str(self.data))

class Graph:

    #dict<String, Vertex>
    def __init__(self):
        self.vertices = {}
        self.size = 0

    def addVertex(self, name):
        newvertex = Vertex(name)
        vertices[name] = newvertex
        size += 1

    def getVertex(self, name):
        if name in vertices.keys():
            return vertices[name]
        return None

    def getVertices(self):
        return self.vertices

    def addEdge(self, name1, name2, weight=0):
        if name1 in self.vertices.keys() and name2 in self.vertices.keys():
            v1 = self.vertices[name1]
            v2 = self.vertices[name2]
            v1.addEdge(v2.getName(), weight)
            v2.addEdge(v1.getName(), weight)
        return
