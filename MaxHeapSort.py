import MaxHeap as mh

def MaxHeapSort(array):
    maxHeap = mh.MaxHeap(array)
    heapSize = len(maxHeap.heap) - 1
    while(heapSize >= 1):
        maxHeap.swap(0, heapSize, maxHeap.heap)
        heapSize = heapSize - 1
        maxHeap.siftDown(0, heapSize, maxHeap.heap)
    return maxHeap.heap

print(MaxHeapSort([10, 2, 123, 3, 14, 53, 657, 8, 192, 1320]))
