import tsGraph as tsg

def topologicalSort(vertices, edgeList):
    tsGraph = createGraph(vertices, edgeList)
    return SortNodes(tsGraph)

def createGraph(vertices, edgeList):
    graph = tsg.tsGraph(vertices)
    # [x, y] x->y x is indegree of y
    for inDegree, node in edgeList:
        graph.addInDegree(node, inDegree, -1)
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
    for inDegreeNode in node.inDegreeNodes:
        containsCycle = depthFirstTraverse(inDegreeNode, orderedNodes)
        if containsCycle:
            return True # Cannot be topologically sorted        
    node.visited = True
    node.inProgress = False # Not needed but clean
    orderedNodes.append(node.vertex)
    return False

# dataSet = open("C:\\Users\\Umma\\Downloads\\input.txt", "r")

# vertices, edges = map(int, dataSet.readline().split(' '))

# edgeList = [map(int, line.split(' ')) for line in dataSet]
# for vertex1, vertex2 in edgeList:
#     print(vertex1, vertex2)

# dataSet.close()

# Create list of our nodes for ease of use
# verticesList = [*range(1, vertices + 1)]
verticesList = [1, 2, 3, 4, 5, 6, 7]
edgeList = ((1, 2), 
(1, 3), 
(3, 4), 
(2, 5), 
(5, 6), 
(3, 7))
# print(verticesList)

topSorted = topologicalSort(verticesList, edgeList)
print(topSorted)

# output = open("C:\\Users\\Umma\\Downloads\\output.txt", "x")
# for i in range(len(topSorted)):
#     output.write(str(topSorted[i]) + " ")
# output.close()
