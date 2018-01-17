class Vertex:

    def __init__(self, name):
        self.name = name
        self.data = None
        self.children = []

    def getName(self):
        return self.name

    def getData(self):
        return self.data

    def getChildren(self):
        return children

    def setName(self, newname):
        self.name = newname

    def setData(self, newdata):
        self.data = newdata

    #connecting = name of the node connecting to
    def addChild(self, connecting):
        self.children.append(connecting)

    def __str__(self):
        return(str(self.name) + ":\t" + str(self.data))


class ListGraph:

    def __init__(self):
        self.nodes = []

    def addNode(self, name):
        newNode = Vertex(name)
        self.nodes.append(newNode)

    def getNodes(self):
        return self.nodes
