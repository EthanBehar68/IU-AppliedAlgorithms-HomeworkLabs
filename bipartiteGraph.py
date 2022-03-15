class bipartiteGraph:
    def __init__(self, vertices):
        self.nodes = []
        self.graph = {}
        for vertex in vertices:
            self.addNode(vertex)

    def addNode(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = bipartiteGraphNode(vertex)
            self.nodes.append(self.graph[vertex])

    def getNode(self, vertex):
        if vertex not in self.graph:
            self.addNode(vertex)
        return self.graph[vertex]

    def addAdjacentNode(self, vertex, adjacentVertex):
        node = self.getNode(vertex)
        adjacentNode = self.getNode(adjacentVertex)
        if not adjacentNode in node.adjacentNodes:
            node.adjacentNodes.append(adjacentNode)
        if not node in adjacentNode.adjacentNodes:
            adjacentNode.adjacentNodes.append(node)

class bipartiteGraphNode():
    def __init__ (self, vertex):
        self.vertex = vertex
        self.adjacentNodes = []
        self.visited = False
        self.inProgress = False
        self.color = "Black"