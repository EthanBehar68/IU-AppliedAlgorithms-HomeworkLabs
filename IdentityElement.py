#Question at hand
#Given a sorted array of distinct integers A[1..n], 
#you want to find out if there is an index i for which A[i] = i. 
#Devise a divide-and-conquer algorithm that runs in time O(log n)​

def IdentityElement(array, start, end):
    middle = end - ((end-start) // 2)
    print("Searching middle point: " + str(middle))

    #Base case for recursion / not found
    if end < start:
        print("No identity element found.")
        return False
    #Pre-process Conquer
    if array[middle] == middle:
        print("Found identity element " + str(middle) + ".")
        return True
    #Divide and go to lower half
    elif array[middle] > middle:
        print("Searching lower half of array")
        return IdentityElement(array, start, middle-1)
    #Divide and go to upper half
    else:
        print("Searching upper half of array")
        return IdentityElement(array, middle+1, end)

array = [1, 7, 8, 9, 10, 11]
print(IdentityElement(array, 0, len(array)))
