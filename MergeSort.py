#I used this one for Rosalind#
def MergeSort(array, length):
    return MergeSortDivide(array, length)


def MergeSortDivide(array, length):
    if length == 1:
        return array
    else:
	    middle = length // 2
	    #Divide
	    left = array[:middle]
	    right = array[middle:]
	    #Conquer
	    array = MergeSortConquer(MergeSortDivide(left, len(left)), MergeSortDivide(right, len(right)))
	    return array	
	
    
def MergeSortConquer(left, right):
    combinedSortedArray = []
    while left and right:
        l = left[0]
        r = right[0]
        if l <= r:
            combinedSortedArray.append(l)
            left.remove(l)
        else:
            combinedSortedArray.append(r)
            right.remove(r)
    
    while left:
        combinedSortedArray.append(left[0])
        left.remove(left[0])
    
    while right: 
        combinedSortedArray.append(right[0])
        right.remove(right[0])    
        
    return combinedSortedArray


dataSet = open("C:\\Users\\Umma\\Downloads\\input.txt", "r")

size = int(dataSet.readline())
unsorted = [int(i) for i in dataSet.readline().split(" ")]

dataSet.close()

sorted = MergeSort(unsorted, size)

output = open("C:\\Users\\Umma\\Downloads\\output.txt", "a")
for i in range(len(sorted)):
    output.write(str(sorted[i]) + " ")
output.close()




###Using Auxiliary Array to reduce space complexity to O(n) instead of O(nlogn)###
# def mergeSort(array, length):
#     if length <= 1:
#         return array
    
#     auxArray = array[:]
#     MergeSortDivide(array, 0, length-1, auxArray)
    
#     return array

# def MergeSortDivide(array, start, end, auxArray):
#     if start == end:
#         return
    
#     middle = (start + end) // 2
    
#     #Divide
#     MergeSortDivide(auxArray, start, middle, array)
#     MergeSortDivide(auxArray, middle+1, end, array)
    
#     #Conquer
#     MergeSortConquer(array, start, middle, end, auxArray)
    
# def MergeSortConquer(array, start, middle, end, auxArray):
#     l = start
#     r = middle + 1
#     i = start
#     while l <= middle and r <= end:
#         if auxArray[l] <= auxArray[r]:
#             array[i] = auxArray[l]
#             l += 1
#         else:
#             array[i] = auxArray[r]
#             r += 1
#         i += 1
    
#     while l <= middle:
#         array[i] = auxArray[l]
#         l += 1
#         i += 1
    
#     while r <= end: 
#         array[i] = auxArray[r]
#         r += 1
#         i += 1

