import msGraph as msg

def topologicalSort(vertices, edgeList):
    msGraph = createGraph(vertices, edgeList)
    return SortNodes(msGraph)

def createGraph(vertices, edgeList):
    graph = msg.msGraph(vertices)
    for node, inDegree in edgeList:
        graph.addInDegree(node, inDegree)
    return graph

def SortNodes(graph):
    orderedNodes = []
    nodes = graph.nodes
    while len(nodes):
        node = nodes.pop()
        containsCycle = depthFirstTraverse(node, orderedNodes)
        if containsCycle:
            return [] # cannot be topologically sorted
    return orderedNodes

def depthFirstTraverse(node, orderedNodes):
    if node.visited:
        return False # Node already accounted for, move to next
    if node.inProgress:
        return True # Signals a cycle so bail
    node.inProgress = True
    for inDegreeNode in node.outgoingNodes:
        containsCycle = depthFirstTraverse(inDegreeNode, orderedNodes)
        if containsCycle:
            return True # Cannot be topologically sorted        
    node.visited = True
    node.inProgress = False # Not needed but clean
    orderedNodes.append(node)
    return False