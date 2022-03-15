############
#Question 1#
############
#Given the input of k sorted arrays, each containing N distinct integers in increasing order, 
#devise an O(kN) algorithm to output the number of integers that appear in each of the k input arrays.
#[1, 3, 5], [1, 2, 3], [1, 5, 7] = 1 (as in one number(1) appears in all of these arrays)
#[1, 3, 5], [1, 2, 3], [1, 3, 7] = 2 (as in two numbers(1, 3) appear in all of these arrays)
#
#Asked Chao-Hong Chen for help via e-mails
#Once you figure the case of 3 arrays out, it is not hard to see what happen when there are k arrays.
#Like the case of 3 arrays, you will need to maintain one index for each array which might be stored in an array Index[0:k].
#In every iteration, either all index point to the same number (if kSortedArrays[i][Index[i]] == kSortedArrays[j][Index[j]] for all i,j < k 
#then samIntegerCount += 1) or you need to increment the index which points to the smallest value.
#To keep it under O(kN), you can accomplish this by finding common numbers for two arrays at a time

# First try but it is hardcoded
# i, j, l = 0, 0, 0
# sameIntegerCount = 0
# while i < nLength and j < nLength and l < nLength:
#     if(kSortedArrays[0][i] == kSortedArrays[1][j] == kSortedArrays[2][l]):
#         i += 1
#         j += 1
#         l += 1
#         sameIntegerCount += 1
#     elif (kSortedArrays[0][i] <= kSortedArrays[1][j] and kSortedArrays[0][i] <= kSortedArrays[2][l]):
#         i += 1
#     elif (kSortedArrays[1][j] <= kSortedArrays[0][i] and kSortedArrays[1][j] <= kSortedArrays[2][l]):
#         j += 1
#     elif (kSortedArrays[2][l] <= kSortedArrays[0][i] and kSortedArrays[2][l] <= kSortedArrays[1][j]):
#         l += 1
# return sameIntegerCount

def Question1(kSortedArrays, kLength, nLength):
    kIndices = [0] * kLength

    sameIntegerCount = 0
    smallestIndex = 0

    done = False
    while not done:
        allSame = True
        for k in range(0, kLength-2, 1):
            if kSortedArrays[k][kIndices[k]] == kSortedArrays[k+1][kIndices[k+1]] and kSortedArrays[k+1][kIndices[k+1]] == kSortedArrays[k+2][kIndices[k+2]]:
                continue
            else:
                allSame = False
                break

        #If all same we can incrememt all indices by one.
        if allSame:
            sameIntegerCount += 1
            if kIndices[k] == nLength-1:
                done = True
                break
            for k in range(0, kLength, 2):
                kIndices[k] = min(kIndices[k]+1, nLength-1)
                if k < kLength-1: #Does this actually same any costs?
                    kIndices[k+1] = min(kIndices[k+1]+1, nLength-1)
            continue

        #Find Smallest Index
        for k in range(kLength):
            if kSortedArrays[smallestIndex][kIndices[smallestIndex]] >= kSortedArrays[k][kIndices[k]]:
                smallestIndex = k
        
        for k in range(kLength):
            if smallestIndex != k:
                if kSortedArrays[smallestIndex][kIndices[smallestIndex]] >= kSortedArrays[k][kIndices[k]]:
                    kIndices[k] = min(kIndices[k]+1, nLength-1)


        kIndices[smallestIndex] = kIndices[smallestIndex]+1
        if kIndices[smallestIndex] >= nLength:
            done = True
        
        allMax = all(ele == nLength for ele in kIndices)
        if allMax:
            done = True
    
    return sameIntegerCount

kSortedArrays = [[1, 3, 5], [1, 2, 3], [0, 1, 7]]
kLength = 3
nLength = 3
print("Question 1 with input " + str(kSortedArrays) + ". Answer is " + str(Question1(kSortedArrays, kLength, nLength)))
kSortedArrays = [[1, 3, 5], [1, 2, 3], [1, 5, 7]]
kLength = 3
nLength = 3
print("Question 1 with input " + str(kSortedArrays) + ". Answer is " + str(Question1(kSortedArrays, kLength, nLength)))
kSortedArrays = [[1, 3, 5, 9], [1, 2, 3, 9], [1, 3, 7, 9], [1, 2, 5, 9]]
kLength = 4
nLength = 4
print("Question 1 with input " + str(kSortedArrays) + ". Answer is " + str(Question1(kSortedArrays, kLength, nLength)))
kSortedArrays = [[1, 10, 20, 30, 40, 50, 60, 70], [1, 30, 31, 32, 33, 34, 40, 50], [30, 50, 55, 65, 75, 105, 125, 135]]
kLength = 3
nLength = 8
print("Question 1 with input " + str(kSortedArrays) + ". Answer is " + str(Question1(kSortedArrays, kLength, nLength)))

############
#Question 2#
############
#An array A[1..n] contains all integers from 0 to n except one number
#Devise an algorithm to determine the missing integer in O(n) time.
#Used this to help me come up with a solution: https://stackoverflow.com/questions/61088969/find-the-missing-number-from-an-unsorted-array-using-divide-and-conquer-and-medi
def Question2(unsortedArray, nLength):
    low, high = 0, len(unsortedArray)

    while low < high:
        middle = (low + high + 1) // 2
        smaller = sum(i < middle for i in unsortedArray)

        if smaller < middle:
            high = middle - 1
        else:
            low = middle
    return low

n = 9
unsortedArray = [1, 2, 8, 7, 5, 4, 3, 9, 0] 
print("Question2 with input " + str(unsortedArray) + ". Answer is " + str(Question2(unsortedArray, n))) #6
unsortedArray = [1, 2, 8, 7, 5, 4, 3, 9, 6] 
print("Question2 with input " + str(unsortedArray) + ". Answer is " + str(Question2(unsortedArray, n))) #0
unsortedArray = [1, 2, 8, 6, 5, 4, 3, 9, 0] 
print("Question2 with input " + str(unsortedArray) + ". Answer is " + str(Question2(unsortedArray, n))) #7
unsortedArray = [6, 2, 8, 7, 5, 4, 3, 9, 0] 
print("Question2 with input " + str(unsortedArray) + ". Answer is " + str(Question2(unsortedArray, n))) #1




############
#Question 4#
############
#You are given two sorted lists of size m and n. 
#Devise an O(log m + logn) time algorithm for 
#computing the kth smallest element in the union of the two list
#Had to use this for help: https://stackoverflow.com/questions/4607945/how-to-find-the-kth-smallest-element-in-the-union-of-two-sorted-arrays
#And: https://www.geeksforgeeks.org/k-th-element-two-sorted-arrays/
def Question4(kthSmallest, m, n, mIndex, nIndex, mLength, nLength):
    #Invalid case
    if kthSmallest > (mLength + nLength):
        return "Invalid"

    # The Base Case/Conquer
    if(mIndex + nIndex == kthSmallest - 1):
        if mLength > mIndex and (nLength <= nIndex or m[mIndex] < n[nIndex]):
            return m[mIndex]
        else:
            return n[nIndex]
    #Divide/Recurse
    step = (kthSmallest - mIndex - nIndex) // 2
    mStep = mIndex + step
    nStep = nIndex + step
    if mLength > mStep - 1 and (nLength <= nStep - 1 or m[mStep - 1] < n[nStep - 1]):
        mIndex = mStep
    else:
        nIndex = nStep
    
    return Question4(kthSmallest, m, n, mIndex, nIndex, mLength, nLength)
    
# m = [1, 2, 3, 4, 5, 6, 10]
# n = [1, 2, 5, 7, 8, 9]
# mLength = 7
# nLength = 6
# kthSmallest = 5
# print("Question with input m:" + str(m) + " and n:" + str(n) + ". Finding " + str(kthSmallest) + " smallest integer. Answer is " + str(Question4(kthSmallest, m, n, 0, 0, mLength, nLength)))

# m = [1, 2, 3, 4, 5, 6, 10]
# n = [1, 2, 5, 7, 8, 9]
# mLength = 7
# nLength = 6
# kthSmallest = 13
# print("Question with input m:" + str(m) + " and n:" + str(n) + ". Finding " + str(kthSmallest) + " smallest integer. Answer is " + str(Question4(kthSmallest, m, n, 0, 0, mLength, nLength)))

# m = [5, 10, 13, 14, 15, 16, 110]
# n = [1, 2, 5, 7, 8, 9]
# mLength = 7
# nLength = 6
# kthSmallest = 7
# print("Question with input m:" + str(m) + " and n:" + str(n) + ". Finding " + str(kthSmallest) + " smallest integer. Answer is " + str(Question4(kthSmallest, m, n, 0, 0, mLength, nLength)))

# m = [5, 10, 13, 14, 15, 16, 110]
# n = [1, 2, 5, 7, 8, 9]
# mLength = 7
# nLength = 6
# kthSmallest = 13
# print("Question with input m:" + str(m) + " and n:" + str(n) + ". Finding " + str(kthSmallest) + " smallest integer. Answer is " + str(Question4(kthSmallest, m, n, 0, 0, mLength, nLength)))

# m = [5, 10, 13, 14, 15, 16, 110]
# n = [1, 2, 5, 7, 8, 9]
# mLength = 7
# nLength = 6
# kthSmallest = 14
# print("Question with input m:" + str(m) + " and n:" + str(n) + ". Finding " + str(kthSmallest) + " smallest integer. Answer is " + str(Question4(kthSmallest, m, n, 0, 0, mLength, nLength)))