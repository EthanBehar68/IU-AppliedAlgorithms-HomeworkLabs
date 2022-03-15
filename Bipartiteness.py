import bipartiteGraph as bg

def IsBipartiteGraph(vertexList, edgeList):
    graph = bg.bipartiteGraph(vertexList)
    for node, adjacent in list(edgeList):
        graph.addAdjacentNode(node, adjacent)
        graph.addAdjacentNode(adjacent, node)

    return BipartiteBreadthFirstSearch(graph)

def BipartiteBreadthFirstSearch(graph):
    queue = []
    sourceNode = graph.getNode(1)
    sourceNode.color = "Red"
    queue.append(sourceNode)

    while queue:
        currentNode = queue.pop(0)
        for adjacentNode in currentNode.adjacentNodes:
            if adjacentNode.color == "Black":
                if currentNode.color == "Black": print("ytup")
                adjacentNode.color = "Blue" if currentNode.color == "Red" else "Red"
                queue.append(adjacentNode)
            else:
                if currentNode.color == adjacentNode.color:
                    return -1
    return 1


dataSet = open("C:\\Users\\Umma\\Downloads\\input.txt", "r")

numberOfGraphs = int(dataSet.readline())
vertexCount = []
edgeLists = []
currentEdgeList = []
firstLine = True
for line in dataSet:
    # New graph start a new edge list
    if line == "\n":
        if currentEdgeList: 
            edgeLists.append(currentEdgeList) 
        currentEdgeList = []
        firstLine = True
    else:
        # Build edge list
        split = line.split(' ')
        if firstLine:
            vertexCount.append(int(split[0]))
            firstLine = False
        else:
            currentEdgeList.append([int(split[0]), int(split[1])])

edgeLists.append(currentEdgeList)

dataSet.close()

bipartitenessTests = []
for i in range(len(edgeLists)):
    verticesList = [*range(1, vertexCount[0] + 1)]
    bipartitenessTests.append(IsBipartiteGraph(verticesList, edgeLists[i]))


output = open("C:\\Users\\Umma\\Downloads\\output.txt", "x")
for i in range(len(bipartitenessTests)):
    output.write(str(bipartitenessTests[i]) + " ")
output.close()