class msGraph:
    def __init__(self, nodes):
        self.nodes = []
        self.graph = {}
        for node in nodes:
            self.addNode(node)

    def addNode(self, node):
        self.graph[node] = msNode(node)
        self.nodes.append(self.graph[node])

    def addInDegree(self, incomingNode, incomingInDegreeNode):
        node = self.getNode(incomingNode)
        inDegreeNode = self.getNode(incomingInDegreeNode)
        node.outgoingNodes.append(inDegreeNode)
        inDegreeNode.incomingNodes.append(node)

    def getNode(self, node):
        if node not in self.graph:
            self.addNode(node)
        return self.graph[node]

class msNode:
    def __init__(self, node):
        self.vertex = node
        self.outgoingNodes = []
        self.incomingNodes = []
        self.visited = False
        self.inProgress = False