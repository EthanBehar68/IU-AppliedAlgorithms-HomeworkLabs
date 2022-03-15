import PriorityQueue as pq
import pqGraph as pqg

def getDijkstrasDistances(vertices, adjacencyList):
    graph = createGraph(vertices, adjacencyList)
    return computeDijkstrasDistances(graph)

def createGraph(vertices, adjacencyList):
    graph = pqg.pqGraph(vertices, adjacencyList)
    return graph

def computeDijkstrasDistances(graph):
    distances = [float('inf')] * len(graph.nodes)
    # setS = []

    sourceNode = graph.getNode(1)
    sourceNode.distanceToSource = 0
    distances[sourceNode.vertex - 1] = 0

    PQ = pq.PriorityQueue(graph.nodes)

    while not PQ.getLength() == 0:
        u = PQ.remove()
        # setS.append(u)

        for v in u.adjacentNodes:
            newDistance = u.distanceToSource + v["weight"]
            if newDistance < v["node"].distanceToSource:
                v["node"].distanceToSource = newDistance
                v["node"].sourceNode = sourceNode
                v["node"].previousNode = u
                distances[v["node"].vertex - 1] = v["node"].distanceToSource
                PQ.siftDown(0, len(PQ.minHeap) - 1, PQ.minHeap)

    distances = [-1 if x == float('inf') else x for x in distances]
    return distances

dataSet = open("C:\\Users\\Umma\\Downloads\\input.txt", "r")

vertices, edges = map(int, dataSet.readline().split(' '))
adjacencyList = {}
for line in dataSet:
    split = line.split(' ')
    if not int(split[0]) in adjacencyList:
        adjacencyList[int(split[0])] = [ {"node": int(split[1]), "weight": int(split[2])} ]
    else:
        adjacencyList[int(split[0])].append( {"node": int(split[1]), "weight": int(split[2])} )

dataSet.close()

# Create list of our nodes for ease of use
verticesList = [*range(1, vertices + 1)]

distances = getDijkstrasDistances(verticesList, adjacencyList)

print(str(distances))

# output = open("C:\\Users\\Umma\\Downloads\\output.txt", "x")
# for i in range(len(distances)):
#     output.write(str(distances[i]) + " ")
# output.close()