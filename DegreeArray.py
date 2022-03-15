def degreeArray(adjacencyList, vertices, edges):
    degree = [0] * vertices

    for vertex in adjacencyList:
            # -1 to make the vertex array based
            degree[vertex - 1] = len(adjacencyList[vertex])
    
    return degree

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

degree = degreeArray(adjacencyList, vertices, edges)

output = open("C:\\Users\\Umma\\Downloads\\output.txt", "x")

for i in range(len(degree)):
    output.write(str(degree[i]) + " ")

output.close()


