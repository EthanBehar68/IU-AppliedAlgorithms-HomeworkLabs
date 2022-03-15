class sccGraph:
    def __init__(self, vertices):
        self.nodes = []
        self.graph = {}
        for vertex in vertices:
            self.addNode(vertex)

    def addNode(self, vertex):
        self.graph[vertex] = sccNode(vertex)
        self.nodes.append(self.graph[vertex])

    def getNode(self, vertex):
        if vertex not in self.graph:
            self.addNode(vertex)
        return self.graph[vertex]

    def addAdjacentNode(self, vertex, adjacentVertex):
        node = self.getNode(vertex)
        adjacentNode = self.getNode(adjacentVertex)
        node.adjacentNodes.append(adjacentNode)
                
class sccNode:
    def __init__(self, vertex):
        self.vertex = vertex
        self.adjacentNodes = []
        self.visited = False
        self.inProgress = False