import bfsGraph as bfs

def getBreadthFirstSearchDistances(vertices, edgeList):
    bfsGraph  = createGraph(vertices, edgeList)
    return computeBreadthFirstSearchDistance(bfsGraph )

def createGraph(vertices, edgeList):
    graph = bfs.bfsGraph(vertices)
    # [x, y] x->y x is adjacent of y
    for node, adjacent in list(edgeList):
        graph.addAdjacentNode(node, adjacent)
    return graph
    
def computeBreadthFirstSearchDistance(graph):
    distances = [-1] * len(graph.nodes)
    queue = []
    
    startNode = graph.getNode(1)
    distances[startNode.vertex - 1] = 0
    queue.append(startNode)

    while queue:
        currentNode = queue.pop(0)
        for adjacentNode in currentNode.adjacentNodes:
            if distances[adjacentNode.vertex - 1] == -1:
                queue.append(adjacentNode)
                distances[adjacentNode.vertex - 1] = distances[currentNode.vertex - 1] + 1

    return distances

dataSet = open("C:\\Users\\Umma\\Downloads\\input.txt", "r")

vertices, edges = map(int, dataSet.readline().split(' '))
edgeList = []
for line in dataSet:
    split = line.split(' ')
    edgeList.append([int(split[0]), int(split[1])])

dataSet.close()

# Create list of our nodes for ease of use
verticesList = [*range(1, vertices + 1)]

searchOrder = getBreadthFirstSearchDistances(verticesList, edgeList)

output = open("C:\\Users\\Umma\\Downloads\\output.txt", "x")
for i in range(len(searchOrder)):
    output.write(str(searchOrder[i]) + " ")
output.close()