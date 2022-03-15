def kthSmallestElement(array, k, size):
    # Make Kth Element 0-Based
    k = k - 1
    return doKthSmallestElement(array, k, 0, size - 1)
	
def doKthSmallestElement(array, k, start, end):
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

    if right == k:
        return array[right]

    if right > k:
        return doKthSmallestElement(array, k, start, right - 1)
    else:
        return doKthSmallestElement(array, k, right + 1, end)

def swap(i, j, array):
        array[i], array[j] = array[j], array[i]

dataSet = open("C:\\Users\\Umma\\Downloads\\input.txt", "r")

size = int(dataSet.readline())
array = [int(i) for i in dataSet.readline().split(" ")]
k = int(dataSet.readline())

dataSet.close()

kthInteger = kthSmallestElement(array, k, size)

output = open("C:\\Users\\Umma\\Downloads\\output.txt", "a")
output.write(str(kthInteger))
output.close()
