import sccGraph as scc

def getStronglyConnectedComponent(vertices, edgeList, timeStack):
    sccGraph = createGraph(vertices, edgeList)
    transposeGraph = createTransposeGraph(vertices, edgeList)
    return getStronglyConnectedComponentCount(sccGraph, transposeGraph, timeStack)

def createGraph(vertices, edgeList):
    graph = scc.sccGraph(vertices)
    # [x, y] x->y x is adjacent of y
    for node, adjacent in list(edgeList):
        graph.addAdjacentNode(node, adjacent)
    return graph

def createTransposeGraph(vertices, edgeList):
    graph = scc.sccGraph(vertices)
    for node, adjacent in list(edgeList):
        graph.addAdjacentNode(adjacent, node)
    return graph
    
def getStronglyConnectedComponentCount(graph, transposeGraph, timeStack):
    sccCount = 0

    for node in graph.nodes:
        depthFirstTraverseTimeStack(node, timeStack)

    while timeStack:
        node = timeStack.pop()
        transposeNode = transposeGraph.getNode(node.vertex)
        if not transposeNode.visited:
            depthFirstTraverse(transposeNode)
            sccCount += 1

    return sccCount

def depthFirstTraverseTimeStack(node, timeStack):
    if node.visited or node.inProgress:
        return # Node already accounted for, move to next
    node.inProgress = True
    for adjacentNode in node.adjacentNodes:
        depthFirstTraverseTimeStack(adjacentNode, timeStack)
    node.visited = True
    node.inProgress = False # Not needed but clean
    timeStack.append(node)

def depthFirstTraverse(node):
    if node.visited or node.inProgress:
        return # Node already accounted for, move to next
    node.inProgress = True
    for adjacentNode in node.adjacentNodes:
        depthFirstTraverse(adjacentNode)
    node.visited = True
    node.inProgress = False # Not needed but clean

# dataSet = open("C:\\Users\\Umma\\Downloads\\input.txt", "r")

# vertices, edges = map(int, dataSet.readline().split(' '))
# edgeList = []
# for line in dataSet:
#     split = line.split(' ')
#     edgeList.append([int(split[0]), int(split[1])])

# dataSet.close()

# # Create list of our nodes for ease of use
# verticesList = [*range(1, vertices + 1)]

# # Stack to help track info to determine Strongly Connect Component
timeStack = [] # as in time to complete depth first traverse

vertices = (1, 2, 3, 4, 5, 6)
edgeList = [(4, 1), (1, 2), (2, 4), (5, 6), (3, 2), (5, 3),
(3, 5)]

sccCount = getStronglyConnectedComponent(vertices, edgeList, timeStack)

print(sccCount)

# output = open("C:\\Users\\Umma\\Downloads\\output.txt", "x")
# output.write(str(sccCount))
# output.close()