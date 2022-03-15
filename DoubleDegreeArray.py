def doubleDegreeArray(adjacencyList, vertices, edges):
    # Double-Degree = number of edges 
    # connected to vertex's adjacent vertices
    doubleDegree = [0] * vertices

    for vertex in adjacencyList:
        for adjacentVertex in adjacencyList[vertex]:
            # -1 to make the vertex array based
            doubleDegree[vertex - 1] += len(adjacencyList[adjacentVertex])
    
    return doubleDegree

dataSet = open("C:\\Users\\Umma\\Downloads\\input.txt", "r")

vertices, edges = map(int, dataSet.readline().split(' '))

edgeList = [map(int, line.split(' ')) for line in dataSet]

dataSet.close()

# Convert Edge List to an Adjacency List
# Makes it easier to compute double degree array
adjacencyList = {e:[] for e in range (1, vertices + 1)}
for vertex1, vertex2 in edgeList:
    adjacencyList[vertex1].append(vertex2)
    adjacencyList[vertex2].append(vertex1)

doubleDegree = doubleDegreeArray(adjacencyList, vertices, edges)

output = open("C:\\Users\\Umma\\Downloads\\output.txt", "x")

for i in range(len(doubleDegree)):
    output.write(str(doubleDegree[i]) + " ")

output.close()


