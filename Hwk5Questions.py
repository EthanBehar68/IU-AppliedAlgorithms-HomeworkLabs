import mstGraph as mstg
import bfsGraph as bfs

# Question 1
print("~~~Question 1~~~")
# These resources helped me understand a feedback edge set.
# https://cstheory.stackexchange.com/questions/36222/minimum-weight-feedback-edge-set-in-undirected-graph-how-to-find-it-is-it-np
# https://softwareengineering.stackexchange.com/questions/261785/min-weight-feedback-edge-set-with-dfs/291621#291621
# https://stackoverflow.com/questions/10791689/how-to-find-feedback-edge-set-in-undirected-graph
# We can use the edges not present in a Min Spanning Tree to construct the max weight feedback edge set.
# Simiarly we can use the edges not present in a Max Spanning Tree to construct the min weight feedback edge set.
vertices = [0, 1, 2, 3, 4, 5, 6, 7, 8]
edgeList = [(0, 1, 1), (0, 2, 2), (0, 8, 3), (1, 2, 4), (1, 3, 3), (2, 8, 5), (2, 4, 2), (2, 3, 4), (3, 4, 5), (3, 5, 2), (3, 6, 3), (6, 7, 4), (4, 8, 1), (4, 5, 1)]
graph = mstg.mstGraph(vertices)
for node, adjacent, weight in edgeList:
    graph.addAdjacentNode(node, adjacent, weight)
    graph.addAdjacentNode(adjacent, node, weight)
graph.buildEdges()

graph.maxWeightFeedbackEdgeSet()
graph.minWeightFeedbackEdgeSet()

# Question 2
# See Document

# Question 3 
# See Document

# Question 4
# See Document
# Additional proof for question 4
# Question 4 Proof - produces the same result as the image in the document
print("~~~Question 4~~~")
vertices = [0, 1, 2, 3, 4]
edgeList = [(0, 1, 1), (0, 2, 6), (0, 3, 8), (1, 4, 2), (1, 3, 15), (2, 3, 10), (2, 4, 5), (3, 4, 11)]
graph = mstg.mstGraph(vertices)
for node, adjacent, weight in edgeList:
    graph.addAdjacentNode(node, adjacent, weight)
graph.buildEdges()

graph.minstKruskal()

# Question 5
# These resources helped me understand diameter of a tree.
# https://www.geeksforgeeks.org/diameter-n-ary-tree-using-bfs/?ref=lbp
# https://www.geeksforgeeks.org/diameter-n-ary-tree/?ref=lbp
# https://www.geeksforgeeks.org/diameter-tree-using-dfs/?ref=lbp
# https://www.geeksforgeeks.org/diameter-of-a-binary-tree/?ref=lbp
# Creating graph is O(V+E)
# Two BFS searches are O(2(V+E)) = O(V+E)
print("~~~Question 5~~~")
def getBreadthFirstSearchDistances(vertices, edgeList, startNode):
    bfsGraph  = createGraph(vertices, edgeList)
    return computeBreadthFirstSearchDistance(bfsGraph , startNode)

def createGraph(vertices, edgeList):
    graph = bfs.bfsGraph(vertices)
    # [x, y] x->y x is adjacent of y
    for node, adjacent in list(edgeList):
        graph.addAdjacentNode(node, adjacent)
        graph.addAdjacentNode(adjacent, node)
    return graph
    
def computeBreadthFirstSearchDistance(graph, startNode):
    distances = [-1] * len(graph.nodes)
    queue = []
    
    startNode = graph.getNode(startNode)
    distances[startNode.vertex] = 0
    queue.append(startNode)

    while queue:
        currentNode = queue.pop(0)
        for adjacentNode in currentNode.adjacentNodes:
            if distances[adjacentNode.vertex] == -1:
                queue.append(adjacentNode)
                distances[adjacentNode.vertex] = distances[currentNode.vertex] + 1

    return distances


vertices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
edgeList = [(0, 1), (1, 3), (3, 7), (3, 5), (5, 9), (9, 11), (0, 2), (2, 4), (4, 6), (4, 8), (8, 10), (10, 12)]
startNode = 0
distances = getBreadthFirstSearchDistances(vertices, edgeList, startNode)
maxDistance = max(distances)
print("Distances from " + str(startNode) + ": " + str(distances))
print(str(maxDistance) + " is " + str(startNode) + " to " + str(distances.index(maxDistance)))
startNode = distances.index(maxDistance)
distances = getBreadthFirstSearchDistances(vertices, edgeList, startNode)
maxDistance = max(distances)
print("Distances from " + str(startNode) + ": " + str(distances))
print(str(maxDistance) + " is " + str(startNode) + " to " + str(distances.index(maxDistance)))
print("Diameter of tree is: " + str(max(distances)))

vertices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
edgeList = [(0, 1), (1, 4), (1, 5), (4, 6), (6, 10), (5, 7), (5, 8), (5, 9), (0, 2), (0, 3), (3, 11), (3, 12), (12, 14), (11, 13), (13, 15), (15, 16)]
startNode = 0
distances = getBreadthFirstSearchDistances(vertices, edgeList, startNode)
maxDistance = max(distances)
print("Distances from " + str(startNode) + ": " + str(distances))
print(str(maxDistance) + " is " + str(startNode) + " to " + str(distances.index(maxDistance)))
startNode = distances.index(maxDistance)
distances = getBreadthFirstSearchDistances(vertices, edgeList, startNode)
maxDistance = max(distances)
print("Distances from " + str(startNode) + ": " + str(distances))
print(str(maxDistance) + " is " + str(startNode) + " to " + str(distances.index(maxDistance)))
print("Diameter of tree is: " + str(max(distances)))

# Question 6
print("~~~Question 6~~~")
# See Document

print("~~~Question 8~~~")
# Uses adjacency matrix representation
class ekGraph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    def BFS(self, s, t, parent):
        # visited / not visited tracking
        visited = [False] * (self.ROW)
        # queue needed for BFS
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop()
            for vertex, weight in enumerate(self.graph[u]):
                # if not visited and there is a edge between the two
                if not visited[vertex] and weight > 0:
                    queue.append(vertex)
                    visited[vertex] = True
                    parent[vertex] = u
        # Reached sink/t?
        return True if visited[t] else False

    def FordFulkersonBFS(self, s, t):
        # Path tracking
        parent = [-1] * self.ROW
        maxFlow = 0
        while self.BFS(s, t, parent):
            pathFlow = float('Inf')
            vertex = t

            while (vertex != s):
                pathFlow = min(pathFlow, self.graph[parent[vertex]][vertex])
                vertex = parent[vertex]
            maxFlow += pathFlow

            v = t
            while (v != s):
                u = parent[v]
                self.graph[u][v] -= pathFlow
                self.graph[v][u] += pathFlow
                v = parent[v]
        return maxFlow

graph = [[0, 16, 13, 0, 0, 0], 
        [0, 0, 10, 12, 0, 0], 
        [0, 4, 0, 0, 14, 0], 
        [0, 0, 9, 0, 0, 20], 
        [0, 0, 0, 7, 0, 4], 
        [0, 0, 0, 0, 0, 0]]
s = 0
t = 5
maxFlow = ekGraph(graph).FordFulkersonBFS(s, t)
print ("The maximum possible flow is " + str(maxFlow)) 

graph = [
[0, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
s = 0
t = 25
maxFlow = ekGraph(graph).FordFulkersonBFS(s, t)
print ("The maximum possible flow is " + str(maxFlow)) 

print("~~~Question 9~~~")
class Graph:
    def __init__(self, vertices, equalities, inequalities):
        self.vertices = vertices
        
        self.equalityEdges = []
        for edge in equalities:
            self.equalityEdges.append(edge)
        self.inequalityEdges = []
        for edge in inequalities:
            self.inequalityEdges.append(edge)
       
        self.counters = [0] * len(self.vertices)
        self.counter = 0
     
        self.time = 0
        self.start = [-1] * len(self.vertices)
        self.end = [-1] * len(self.vertices)
        
        self.color = ["WHITE"] * len(self.vertices)
        self.pie = [None] * len(self.vertices)

    def dfs(self):
        for u in self.vertices:
            self.color[u] = "WHITE"
            self.pie[u] = None
        self.time = 0
        for u in self.vertices:
            if self.color[u] == "WHITE":
                self.dfsVisit(u)


    def dfsVisit(self, u):
        self.time += 1
        self.start[u] = self.time
        self.color[u] = "Gray"
        self.counters[u] = self.counter

        neighbors = [edge[1] for edge in self.equalityEdges if edge[0] == u]
        for v in neighbors:
            if self.color[v] == "WHITE":
                self.pie[v] = u
                self.dfsVisit(v)
            elif self.end[v] == -1:
                # back edge
                continue
            elif self.start[u] < self.start[v]:
                # forward
                continue
            else:
                # cross edge
                self.counter += 1
                self.counters[u] = self.counter

        self.color[u] = "BLACK"
        self.time += 1
        self.end[u] = self.time

    def checkConstraints(self):
        # These two operations can probably be combined
        # to make the algo a little more efficient
        self.dfs()
        for u, v  in self.inequalityEdges:
            if self.counters[u] == self.counters[v]:
                print("Constraints are not satisfied.")
                return False
        print("Constraints are satisfied")
        return True         

vertices = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
equalities = [(0, 1), (0, 2), (0, 3), (1, 6), (2, 7), (3, 4),
(4, 5), (5, 9), (6, 8), (7, 8), (9, 8)]
inequalities = [(1, 3), (7, 9), (0, 6), (0, 8)]
dfsGraph = Graph(vertices, equalities, inequalities)
dfsGraph.checkConstraints()

vertices = (0, 1, 2, 3, 4, 5)
equalities = [(3, 0), (0, 1), (1, 3), (4, 5), (2, 1), (4, 1),
(2, 4)]
inequalities = [(0, 4), (3, 5)]
dfsGraph = Graph(vertices, equalities, inequalities)
dfsGraph.checkConstraints()