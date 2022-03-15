import copy

class PriorityQueue():
    def __init__(self, array):
        self.minHeap = self.buildHeap(copy.deepcopy(array))

    def buildHeap(self, array):
            finalParentIndex = (len(array) - 2) // 2
            for currentIndex in reversed(range(finalParentIndex + 1)):
                self.siftDown(currentIndex, len(array) - 1, array)
            return array

    def siftDown(self, currentIndex, endIndex, minHeap):
        childLeft = currentIndex * 2 + 1
        while childLeft <= endIndex:
            childRight = currentIndex * 2 + 2 if currentIndex * 2 + 2 <= endIndex else -1
            if childRight != - 1 and minHeap[childRight].key < minHeap[childLeft].key:
                indexToSwap = childRight
            else:
                indexToSwap =  childLeft
            if minHeap[indexToSwap].key < minHeap[currentIndex].key:
                self.swap(currentIndex, indexToSwap, minHeap)
                currentIndex = indexToSwap 
                childLeft = currentIndex * 2 + 1
            else:
                break
    
    def siftUp(self, currentIndex, minHeap):
        parentIndex = (currentIndex - 1) // 2
        while currentIndex > 0 and minHeap[currentIndex].key < minHeap[parentIndex].key:
            self.swap(currentIndex, parentIndex, minHeap)
            currentIndex = parentIndex
            parentIndex = (currentIndex - 1) // 2

    def insert(self, value):
        self.minHeap.append(value)
        self.siftUp(len(self.minHeap) - 1, self.minHeap)

    def remove(self):
        self.swap(0, len(self.minHeap) - 1, self.minHeap)
        valueToRemove = self.minHeap.pop()
        self.siftDown(0, len(self.minHeap) - 1, self.minHeap)
        return valueToRemove

    def decreaseKey(self, key, value):
        if key in self.minHeap:
            index = self.minHeap.index(key, 0)
            self.minHeap[index].key = value
            self.siftDown(index, len(self.minHeap) - 1, self.minHeap)

    def inPriortyQueue(self, key):
        return True if key in self.minHeap else False

    def peek(self):
        return self.minHeap[0]

    def parent(self, index): 
        return (index - 1) // 2

    def getLength(self):
        return len(self.minHeap)

    def swap(self, i, j, minHeap):
        minHeap[i], minHeap[j] = minHeap[j], minHeap[i]
