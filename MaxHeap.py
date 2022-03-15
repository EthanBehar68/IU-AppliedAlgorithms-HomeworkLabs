class MaxHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)
    
    def buildHeap(self, array):
        finalParentIndex = (len(array) - 2) // 2
        for currentIndex in reversed(range(finalParentIndex + 1)):
            self.siftDown(currentIndex, len(array) - 1, array)
        return array

    def siftDown(self, currentIndex, endIndex, heap):
        childLeft = currentIndex * 2 + 1
        while childLeft <= endIndex:
            childRight = currentIndex * 2 + 2 if currentIndex * 2 + 2 <= endIndex else -1
            if childRight != - 1 and heap[childRight] > heap[childLeft]:
                indexToSwap = childRight
            else:
                indexToSwap =  childLeft
            if heap[indexToSwap] > heap[currentIndex]:
                self.swap(currentIndex, indexToSwap, heap)
                currentIndex = indexToSwap
                childLeft = currentIndex * 2 + 1
            else:
                break
        
    def siftUp(self, currentIndex, heap):
        parentIndex = (currentIndex - 1) // 2
        while currentIndex > 0 and heap[currentIndex] > heap[parentIndex]:
            self.swap(currentIndex, parentIndex, heap)
            currentIndex = parentIndex
            parentIndex = (currentIndex - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

# maxHeap = MaxHeap([10, 2, 123, 3, 14, 53, 657, 8, 192, 1320])

# print(maxHeap.heap)