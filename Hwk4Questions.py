# Question 1
#In document


# Question 2
# This stackoverflow question helped me: https://stackoverflow.com/questions/16124844/algorithm-for-finding-a-hamilton-path-in-a-dag
# Plus read up on hamilton path's: https://www.geeksforgeeks.org/mathematics-euler-hamiltonian-paths/
import hpTopologicalSorting as hpTS # File from topological sorting lab assignment
def HamiltonPathOnDag(vertexList, edgeList):
    # O(V+E) operation
    # sortedNodes is a list of nodes
    sortedNodes = hpTS.topologicalSort(vertexList, edgeList)

    # O(V)
    sortedNodes.reverse()

    # Check if there are edges between consecutive vertices
    # e.g. (1,2), (2,3), ..., (n-1,n).
    # O(V)
    hamiltonPath = True
    for node in sortedNodes:
        if node.vertex < len(sortedNodes):
            if not node.vertex + 1 == sortedNodes[node.vertex].vertex:
                hamiltonPath = False
    return hamiltonPath

# Supplying vertices in reverse order 
# makes dealing with them later easier
# This is b/c of how my graph and topological sort are implemented
vertexList = [4, 3, 2, 1]
edgeList = [(1, 2), (2, 3), (3, 4), (2,4), (1, 3)]
print("Contains hamilton path: " + str(HamiltonPathOnDag(vertexList, edgeList)))
vertexList = [4, 3, 2, 1]
edgeList = [(1, 4), (2, 3), (3, 4), (2,4), (1, 3)]
print("Contains hamilton path: " + str(HamiltonPathOnDag(vertexList, edgeList)))

# Question 3
# https://en.wikipedia.org/wiki/Bipartite_graph
# Basic idea from below: https://www.geeksforgeeks.org/bipartite-graph/
# 1. Assign RED color to the source vertex (putting into set U).
# 2. Color all the neighbors with BLUE color (putting into set V).
# 3. Color all neighbor’s neighbor with RED color (putting into set U).
# 4. This way, assign color to all vertices such that it satisfies all the constraints of m way coloring problem where m = 2.
# 5. While assigning colors, if we find a neighbor which is colored with same color as current vertex, then the graph cannot be colored with 2 vertices (or graph is not Bipartite) 
import bipartiteGraph as bg
def IsBipartiteGraph(vertexList, edgeList):
    graph = bg.bipartiteGraph(vertexList)
    for node, adjacent in list(edgeList):
        graph.addAdjacentNode(node, adjacent)

    return BipartiteBreadthFirstSearch(graph)

def BipartiteBreadthFirstSearch(graph):
    queue = []
    sourceNode = graph.getNode(1)
    sourceNode.color = "Red"
    queue.append(sourceNode)

    isBipartite = True
    while queue:
        currentNode = queue.pop(0)
        for adjacentNode in currentNode.adjacentNodes:
            if adjacentNode.color == "Black":
                adjacentNode.color = "Blue" if currentNode.color == "Red" else "Red"
                queue.append(adjacentNode)
            else:
                if currentNode.color == adjacentNode.color:
                    return False
    return isBipartite

# Uses last graph from question 2
print("Is graph a bipartite graph: " + str(IsBipartiteGraph(vertexList, edgeList)))
# This is a bipartite graph
vertexList = [1, 2, 3, 4, 5, 6]
edgeList = [(1,2), (2,3), (3,4), (4,5), (5,6), (6,1)]
print("Is graph a bipartite graph: " + str(IsBipartiteGraph(vertexList, edgeList)))

# Question 4
# This helped me: https://quizlet.com/491176307/csci570-flash-cards/
# Run topological sort to get an order of vertices to complete the graph aka courses O(V+E)
# Iterate over the list of vertices from the topological sort, if the vertex doesn't have any incoming edges the length = 0, 
# if it does have incoming edges then length(v) = max(length(x) + 1) where x is the previous vertex. we will then get semesters = 1+max(length(v))
import msGraph as ms
import msTopologicalSorting as msTS
def minimumSemesters(vertexList, edgeList):
    # O(V+E) operation
    # sortedNodes is a list of nodes
    sortedNodes = msTS.topologicalSort(vertexList, edgeList)

    sortedNodes.reverse()
    lengths = [1] * len(sortedNodes)

    # O(V) operation... maybe O(V+E) b/c of incomingVertices assignment operation (line 112)
    for node in sortedNodes:
        if node.incomingNodes:
            incomingVertices = (v.vertex-1 for v in node.incomingNodes)
            lengths[node.vertex - 1] = max( [lengths[index] for index in incomingVertices]) + 1

    return str(max(lengths))

vertexList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
edgeList = [(1,2), (2,4), (3,10), (4,9), (5,6)]
print("Minimum # of semesters needed: " + minimumSemesters(vertexList, edgeList))
edgeList = [(1,2), (2,3), (3,4), (4,5), (5,6), (6,7), (7,8), (8, 9), (9, 10)]
print("Minimum # of semesters needed: " + minimumSemesters(vertexList, edgeList))
print("Minimum # of semesters needed: " + minimumSemesters(vertexList, []))

#Question 5
# In document

# Question 6
# I supplied two answers one using Dijkstras and one using FloydWarshall
# These links help me complete the solution plus the Floyd-Warshall section in the class book.
# https://stackoverflow.com/questions/3911626/find-cycle-of-shortest-length-in-a-directed-graph-with-positive-weights
# https://stackoverflow.com/questions/47491806/find-the-lowest-weight-cycle-in-a-weighted-directed-graph-using-dijkstras
# https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
import PriorityQueue as pq
import pqGraph as pqg
def computeShortestCycleWithDijkstras(graph):
    distances = [float('inf')] * len(graph.nodes)
    distances = [[float('inf') for i in range(len(graph.nodes))] for j in range(len(graph.nodes))]

    for v in graph.nodes:
        sourceNode = graph.getNode(v.vertex)
        sourceNode.distanceToSource = 0
        distances[sourceNode.vertex - 1][sourceNode.vertex - 1] = 0
        PQ = pq.PriorityQueue(graph.nodes)

        while not PQ.getLength() == 0:
            u = PQ.remove()
            for v in u.adjacentNodes:
                newDistance = u.distanceToSource + v["weight"]
                if newDistance < v["node"].distanceToSource:
                    v["node"].distanceToSource = newDistance
                    distances[sourceNode.vertex - 1][v["node"].vertex - 1] = v["node"].distanceToSource
                    # Maintain Min-Heap
                    PQ.siftDown(0, len(PQ.minHeap) - 1, PQ.minHeap)
                # Modify Dijkstra's Algorithm to compute cycles
                if  any(ad["node"].vertex == sourceNode.vertex for ad in v["node"].adjacentNodes):
                        if sourceNode.distanceToSource == 0:
                            distances[sourceNode.vertex - 1][sourceNode.vertex - 1] = v["node"].distanceToSource + v["weight"]
                        else:
                            newDistance = v["node"].distanceToSource + v["weight"]
                            if newDistance < distances[sourceNode.vertex - 1][sourceNode.vertex - 1]:
                                 distances[sourceNode.vertex - 1][sourceNode.vertex - 1] = newDistance
  
        # Reset distances for next iteration
        for n in graph.nodes: n.distanceToSource = float('inf')

    cycles = []
    for v in graph.nodes:
        i = v.vertex - 1
        cycles.append(distances[i][i])

    shortestCycle = min(cycles)
    return shortestCycle if not (shortestCycle == float('inf') or shortestCycle == 0) else "No Cycle"

def computeShortestCycleWithFloydWarshall(graph):
    # Need to convert to matrix for this problem
    adjacencyMatrix = [[float('inf') for i in range(len(graph.nodes))] for j in range(len(graph.nodes))]
    for u in graph.nodes:
            for v in u.adjacentNodes:
                adjacencyMatrix[u.vertex-1][v["node"].vertex-1] = v["weight"]

    # Floyd-Warshall Algorithm solves all pairs shortest paths
    for k in range(len(graph.nodes)):
        for i in range(len(graph.nodes)):
            for j in range (len(graph.nodes)):
                adjacencyMatrix[i][j] = min(adjacencyMatrix[i][j], adjacencyMatrix[i][k] + adjacencyMatrix[k][j])

    cycles = []
    for v in graph.nodes:
        i = v.vertex - 1
        cycles.append(adjacencyMatrix[i][i])

    shortestCycle = min(cycles)
    return shortestCycle if not (shortestCycle == float('inf') or shortestCycle == 0) else "No Cycle"


vertexList = [1, 2, 3, 4]
adjacencyList = {
    1 : [ {"node": 2, "weight": 10 }, {"node": 3, "weight": 10 } ],
    2 : [ {"node": 4, "weight": 5 } ],
    3 : [ {"node": 4, "weight": 5 } ],
    4 : [ ]
}
print("Shortest Cycle via Dijkstra's: " + str(computeShortestCycleWithDijkstras(pqg.pqGraph(vertexList, adjacencyList))))
print("Shortest Cycle via Floyd-Warshall's: " + str(computeShortestCycleWithFloydWarshall(pqg.pqGraph(vertexList, adjacencyList))))
vertexList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
adjacencyList = {
    1 : [ {"node": 2, "weight": 10 }, {"node": 6, "weight": 10 } ],
    2 : [ {"node": 3, "weight": 5 } ],
    3 : [ {"node": 4, "weight": 5 }, {"node": 9, "weight": 1 } ],
    4 : [ {"node": 1, "weight": 5 } ],
    5 : [ {"node": 4, "weight": 10 } ],
    6 : [ {"node": 7, "weight": 10 } ],
    7 : [ {"node": 8, "weight": 30 } ],
    8 : [ {"node": 5, "weight": 40 } ],
    9 : [ {"node": 10, "weight": 1 } ],
    10 : [ {"node": 3, "weight": 1 }, {"node": 5, "weight": 20 } ]
}
print("Shortest Cycle via Dijkstra's: " + str(computeShortestCycleWithDijkstras(pqg.pqGraph(vertexList, adjacencyList))))
print("Shortest Cycle via Floyd-Warshall's: " + str(computeShortestCycleWithFloydWarshall(pqg.pqGraph(vertexList, adjacencyList))))



# Question 7 A
# Given the limitation of your car’s fuel tank capacity, 
# show how to determine in linear time whether there is a feasible route from s to t . 
# Solution: This can be done by performing DFS (or BFS) from s ignoring edges of weight larger than L .
def computePathWithWeightLimit(graph, targetNode, limit):
    targetNode = graph.getNode(targetNode)
    nodes = graph.nodes
    print("Can we reach " + str(targetNode.vertex) + " from " + str(graph.getNode(1).vertex))
    while len(nodes):
        node = nodes.pop()
        depthFirstTraverseWithLimint(node, targetNode, limit)

def depthFirstTraverseWithLimint(node, targetNode, limit):
    if node.visited:
        return # Node already accounted for, move to next
    if node.inProgress:
        return # Signals a cycle so bail
    node.inProgress = True
    for adjacentNode in node.adjacentNodes:
        if adjacentNode["weight"] <= limit:
            depthFirstTraverseWithLimint(adjacentNode["node"], targetNode, limit)
            if adjacentNode["node"].vertex == targetNode.vertex:
                print(str(targetNode.vertex) + " can be reached from source.")
    node.visited = True
    node.inProgress = False # Not needed but clean

fuelCapcity = 15
computePathWithWeightLimit(pqg.pqGraph(vertexList, adjacencyList), 5, fuelCapcity)
computePathWithWeightLimit(pqg.pqGraph(vertexList, adjacencyList), 10, fuelCapcity)
computePathWithWeightLimit(pqg.pqGraph(vertexList, adjacencyList), 4, fuelCapcity)
computePathWithWeightLimit(pqg.pqGraph(vertexList, adjacencyList), 8, fuelCapcity)

# Question B A
def computeMaxLengthEdgeDijkstra(graph):
    distances = [float('inf')] * len(graph.nodes)

    sourceNode = graph.getNode(1)
    sourceNode.distanceToSource = 0
    distances[sourceNode.vertex - 1] = 0

    PQ = pq.PriorityQueue(graph.nodes)

    while not PQ.getLength() == 0:
        u = PQ.remove()

        for v in u.adjacentNodes:
            if distances[v["node"].vertex - 1] > max(distances[u.vertex - 1], u.distanceToSource + v["weight"]):
                v["node"].distanceToSource = max(u.distanceToSource, u.distanceToSource + v["weight"])
                distances[v["node"].vertex - 1] = v["node"].distanceToSource
                PQ.siftDown(0, len(PQ.minHeap) - 1, PQ.minHeap)

    return distances

print(computeMaxLengthEdgeDijkstra(pqg.pqGraph(vertexList, adjacencyList)))