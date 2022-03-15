class longestPathGraph:
    def __init__(self, nodes):
        self.nodes = []
        self.graph = {}
        for node in range(nodes+1):
            self.addNode(node)

    def addNode(self, node):
        self.graph[node] = longestPathNode(node)
        self.nodes.append(self.graph[node])

    def addAdjacentNode(self, vertex, adjacentVertex, weight):
        node = self.getNode(vertex)
        adjacentNode = self.getNode(adjacentVertex)
        node.adjacentNodes.append(adjacentNode)
        node.adjacentWeights[adjacentNode.vertex] = weight

    def getNode(self, node):
        if node not in self.graph:
            self.addNode(node)
        return self.graph[node]

class longestPathNode:
    def __init__(self, node):
        self.vertex = node
        self.adjacentNodes = []
        self.adjacentWeights = {}
        self.visited = False
        self.inProgress = False