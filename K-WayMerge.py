#Question at hand
#Suppose you are given k sorted arrays, 
#each with n elements, 
#and you want to combine them into a single sorted array of kn elements.

def kWayMerge(kSortedArrays):
    length = len(kSortedArrays)

    mergedArrays = []

    if length == 1:
       return kSortedArrays[0]
    else:
        for i in range(0, length, 2):
            if i+1 < length:
                mergedArrays.append(MergeArrays(kSortedArrays[i], kSortedArrays[i+1]))
    
    if length % 2 == 1:
        mergedArrays.append(kSortedArrays[length-1])

    return kWayMerge(mergedArrays)


def MergeArrays(left, right):
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

kSortedArrays = [[10, 11, 22, 23, 26, 33], [1, 4, 22, 123, 124, 740], [-21, 15, 30, 65, 101, 1000], [-1, 0, 1, 2, 3, 4], [-10, 30, 970, 975, 980, 990]]

combined = kWayMerge(kSortedArrays)

print(combined)