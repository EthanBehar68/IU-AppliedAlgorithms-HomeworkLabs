class pqGraph:
    def __init__(self, vertices, adjacencyList):
        self.nodes = []
        self.graph = {}
        for vertex in vertices:
            self.addNode(vertex)
            if vertex in adjacencyList:
                for adjacentVertexAndWeight in adjacencyList[vertex]:
                    self.addAdjacentNode(vertex, adjacentVertexAndWeight["node"], adjacentVertexAndWeight["weight"])

    def addNode(self, vertex):
        if not vertex in self.graph:
            self.graph[vertex] = PriorityQueueNode(vertex)
            self.nodes.append(self.graph[vertex])

    def getNode(self, vertex):
        if not vertex in self.graph:
            self.addNode(vertex)
        return self.graph[vertex]

    def addAdjacentNode(self, vertex, adjacentVertex, priority):
        node = self.getNode(vertex)
        adjacentNode = self.getNode(adjacentVertex)
        node.adjacentNodes.append({"node": adjacentNode, "weight": priority})
                
class PriorityQueueNode():
    def __init__ (self, vertex):
        self.vertex = vertex
        self.adjacentNodes = []
        self.distanceToSource = float('inf')
        self.visited = False
        self.inProgress = False