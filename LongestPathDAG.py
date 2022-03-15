# Modified from Topological Sort Lab
import longestPathGraph as lpg

def topologicalSort(graph):
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
    for adjacentNode in node.adjacentNodes:
        containsCycle = depthFirstTraverse(adjacentNode, orderedNodes)
        if containsCycle:
            return True # Cannot be topologically sorted        
    node.visited = True
    node.inProgress = False # Not needed but clean
    orderedNodes.append(node)
    return False

def computeLongestPath(vertices, edgeList, sourceVertex, targetVertex):
    # Create Graph
    graph = lpg.longestPathGraph(vertices)
    for node, adjacent, weight in edgeList:
        graph.addAdjacentNode(node, adjacent, weight)
    # Create distances array
    distances = [float('-inf')] * len(graph.nodes)
    distances[sourceNode] = 0

    # Sort
    topSort = topologicalSort(graph)
    # Compute distances
    while topSort:
        u = topSort.pop()
        if not distances[u.vertex] == float('-inf'):
            for v in u.adjacentNodes:
                if distances[v.vertex] < distances[u.vertex] + u.adjacentWeights[v.vertex]:
                    distances[v.vertex] = distances[u.vertex] + u.adjacentWeights[v.vertex]

    # Creat transpose
    tGraph = lpg.longestPathGraph(vertices)
    for node, adjacent, weight in edgeList:
        tGraph.addAdjacentNode(adjacent, node, weight)

    # Start a targetVertex and work our way backwards to source with transpose graph
    # This builds our path from source to target.
    longestPath = distances[targetVertex]
    traceString = "->" + str(targetVertex)
    while sourceVertex != targetVertex:
        tNode = tGraph.getNode(targetVertex)
        longestVertex = 0
        nextNode = None
        for v in tNode.adjacentNodes:
            if longestVertex < distances[v.vertex]:
                nextNode = v
        if(nextNode == None):
            nextNode = tGraph.getNode(sourceNode)
            traceString = str(nextNode.vertex) + traceString
        else:
            traceString = "->" + str(nextNode.vertex) + traceString
        targetVertex = nextNode.vertex

    return longestPath, traceString

dataSet = open("C:\\Users\\Umma\\Downloads\\input.txt", "r")

sourceNode = int(dataSet.readline())
targetNode = int(dataSet.readline())
edgeList = []

for line in dataSet:
    firstSplit = line.split("->")
    secondSplit = firstSplit[1].split(":")
    edgeList.append([int(firstSplit[0]), int(secondSplit[0]), int(secondSplit[1])])

longestPath, traceString = computeLongestPath(targetNode, edgeList, sourceNode, targetNode)

output = open("C:\\Users\\Umma\\Downloads\\output.txt", "x")
output.writelines(str(longestPath)+"\n")
output.write(traceString)
output.close()
