import MinHeap as mh

def MinHeapSort(array):
    minHeap = mh.MinHeap(array)
    heapSize = len(minHeap.heap) - 1
    while(heapSize >= 1):
        minHeap.swap(0, heapSize, minHeap.heap)
        heapSize = heapSize - 1
        minHeap.siftDown(0, heapSize, minHeap.heap)
    return minHeap.heap

print(MinHeapSort([10, 2, 123, 3, 14, 53, 657, 8, 192, 1320]))
