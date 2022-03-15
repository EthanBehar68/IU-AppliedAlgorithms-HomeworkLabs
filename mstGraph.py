class mstGraph:
    def __init__(self, nodes):
        self.nodes = []
        self.graph = {}
        self.edges = []
        self.sortedEdges = []
        for node in nodes:
            self.addNode(node)

    def addNode(self, node):
        self.graph[node] = mstNode(node)
        self.nodes.append(self.graph[node])

    def addAdjacentNode(self, vertex, adjacentVertex, weight):
        node = self.getNode(vertex)
        adjacentNode = self.getNode(adjacentVertex)
        node.adjacentNodes.append(adjacentNode)
        node.adjacentWeights[adjacentNode.vertex] = weight

    def buildEdges(self):
        for node in self.nodes:
            for adjacentNode in node.adjacentNodes:
                edge = (node.vertex, adjacentNode.vertex, node.adjacentWeights[adjacentNode.vertex])
                if edge not in self.edges:
                    self.edges.append(edge)

    def getNode(self, node):
        if node not in self.graph:
            self.addNode(node)
        return self.graph[node]

    def minstKruskal(self):
        parent = []
        rank = []
        # This will store the resultant MST
        result = []  
        # An index variable, used for sorted edges
        i = 0
        # An index variable, used for result[]
        e = 0

        # Step 1:  Sort all the edges in non-decreasing order of their weight. If we are not allowed to change the given graph, we can create a copy of graph
        self.sortedEdges = sorted(self.edges, key=lambda item: item[2])
        
        # Create V subsets with single elements
        for node in self.nodes:
            parent.append(node.vertex)
            rank.append(0)
 
        # Number of edges to be taken is equal to V-1
        while e < len(self.nodes) - 1:
 
            # Step 2: Pick the smallest edge and increment the index for next iteration
            u, v, w = self.sortedEdges[i]
            i = i + 1
            x = self.kruskalFind(parent, u)
            y = self.kruskalFind(parent, v)
 
            # If including this edge does't cause cycle, include it in result and increment the indexof result for next edge
            if x != y:
                e = e + 1
                result.append((u, v, w))
                self.kruskalUnion(parent, rank, x, y)
            # Else discard the edge
 
        minimumCost = 0
        print("Edges in the constructed MinST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree" , minimumCost)  
        return result  

    def maxWeightFeedbackEdgeSet(self):
        minST = self.minstKruskal()

        maxWeightFeedbackEdgeSet = []
        for edge in self.edges:
            if not edge in minST and not (edge[1], edge[0], edge[2]) in minST: # Since undirected we have to check if either edge was added already. ie 0,1 or 1,0
                if not (edge[1], edge[0], edge[2]) in maxWeightFeedbackEdgeSet:
                    maxWeightFeedbackEdgeSet.append(edge) # Same as above comment

        maxWeight = 0
        print("Edges in the max weight feedback edge set")
        for u, v, weight in maxWeightFeedbackEdgeSet:
            maxWeight += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Max Weight of feedback set" , maxWeight)  
        return maxWeightFeedbackEdgeSet  

    def maxstKruskal(self):
        parent = []
        rank = []
        # This will store the resultant MST
        result = []  
        # An index variable, used for sorted edges
        i = 0
        # An index variable, used for result[]
        e = 0

        # Step 1:  Sort all the edges in decreasing order of their weight. If we are not allowed to change the given graph, we can create a copy of graph
        self.sortedEdges = sorted(self.edges, key=lambda item: item[2])
        self.sortedEdges.reverse()
        
        # Create V subsets with single elements
        for node in self.nodes:
            parent.append(node.vertex)
            rank.append(0)
 
        # Number of edges to be taken is equal to V-1
        while e < len(self.nodes) - 1:
 
            # Step 2: Pick the smallest edge and increment the index for next iteration
            u, v, w = self.sortedEdges[i]
            i = i + 1
            x = self.kruskalFind(parent, u)
            y = self.kruskalFind(parent, v)
 
            # If including this edge does't cause cycle, include it in result and increment the indexof result for next edge
            if x != y:
                e = e + 1
                result.append((u, v, w))
                self.kruskalUnion(parent, rank, x, y)
            # Else discard the edge
 
        maximumCost = 0
        print("Edges in the constructed MaxST")
        for u, v, weight in result:
            maximumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Maximum Spanning Tree" , maximumCost)  
        return result  

    def minWeightFeedbackEdgeSet(self):
        maxST = self.maxstKruskal()

        minWeightFeedbackEdgeSet = []
        for edge in self.edges:
            if not edge in maxST and not (edge[1], edge[0], edge[2]) in maxST: # Since undirected we have to check if either edge was added already. ie 0,1 or 1,0
                if not (edge[1], edge[0], edge[2]) in minWeightFeedbackEdgeSet:
                    minWeightFeedbackEdgeSet.append(edge) # Same as above comment

        minWeight = 0
        print("Edges in the min weight feedback edge set")
        for u, v, weight in minWeightFeedbackEdgeSet:
            minWeight += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Min Weight of feedback set" , minWeight)  
        return minWeightFeedbackEdgeSet  

    def kruskalFind(self, parent, i):
        if parent[i] == i:
            return i
        return self.kruskalFind(parent, parent[i])
    
    def kruskalUnion(self, parent, rank, x, y):
        xroot = self.kruskalFind(parent, x)
        yroot = self.kruskalFind(parent, y)
 
        # Attach smaller rank tree under root of high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
 
        # If ranks are same, then make one as root and increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

class mstNode:
    def __init__(self, node):
        self.vertex = node
        self.adjacentNodes = []
        self.adjacentWeights = {}
        self.key = float('inf')
        self.pie = None

# vertices = [0, 1, 2, 3]
# edgeList = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
# graph = mstGraph(vertices)
# for node, adjacent, weight in edgeList:
#     graph.addAdjacentNode(node, adjacent, weight)
# graph.buildEdges()

# graph.minstKruskal()
# graph.maxstKruskal()

# Book example!!
# vertices = [a, b, c, d, e, f, g, h, i]
# edgeList = [(a, b, 4), (a, h, 8), 
# (b, h, 11), (b, c, 8), 
# (h, i, 7), (h, g, 1), 
# (i, c, 2), (i, g, 6), 
# (c, d, 7), (c, f, 4), 
# (g, f, 2),
# (d, e, 9), (d, f, 14),
# (f, e, 10)]
# vertices = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# edgeList = [(0, 1, 4), (0, 7, 8), 
# (1, 7, 11), (1, 2, 8), 
# (7, 8, 7), (7, 6, 1), 
# (8, 2, 2), (8, 6, 6), 
# (2, 3, 7), (2, 5, 4), 
# (6, 5, 2),
# (3, 4, 9), (3, 5, 14),
# (5, 4, 10)]

# graph = mstGraph(vertices)
# for node, adjacent, weight in edgeList:
#     graph.addAdjacentNode(node, adjacent, weight)
# graph.buildEdges()

# graph.minstKruskal()




