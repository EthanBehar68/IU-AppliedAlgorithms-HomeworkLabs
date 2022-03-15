def quickSort(array, length):
    return doQuickSort(array, 0, length - 1)
	
def doQuickSort(array, start, end):
    if start >= end:
        return array

    pivot = start
    left = start + 1
    right = end
	
    while right >= left:
        if array[left] > array[pivot] and array[right] < array[pivot]:
            swap(left, right, array)
            
        if array[right] >= array[pivot]:
            right -= 1
        if array[left] <= array[pivot]:
            left += 1

    swap(pivot, right, array)
	
    if right - 1 - start < end - (right + 1):
        doQuickSort(array, start, right - 1)
        doQuickSort(array, right + 1, end)
    else:
        doQuickSort(array, right + 1, end)
        doQuickSort(array, start, right - 1)

    return array

def swap(i, j, array):
        array[i], array[j] = array[j], array[i]


dataSet = open("C:\\Users\\Umma\\Downloads\\input.txt", "r")

size = int(dataSet.readline())
array = [int(i) for i in dataSet.readline().split(" ")]

dataSet.close()

sorted = quickSort(array, size)

output = open("C:\\Users\\Umma\\Downloads\\output.txt", "a")
for i in range(len(sorted)):
    output.write(str(sorted[i]) + " ")
    output.close()
