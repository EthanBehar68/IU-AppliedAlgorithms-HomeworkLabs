
# Based on Professor's second solution from discussion/slides.
def FindMajorityElement(array, n, tiebreaker):
    if n == 0:
        return tiebreaker

    pairs = []
    # abritary pick tiebreaker if it is needed
    if n % 2 == 1:
        tiebreaker = array[-1] #python for last element in array
    
    for i in range(0, n-1, 2):
        if array[i] == array[i+1]:
            pairs.append(array[i])
    
    majorityElement = FindMajorityElement(pairs, len(pairs), tiebreaker)

    if majorityElement == None:
        return -1
    
    meCount = array.count(majorityElement)
    if meCount * 2 > n or (meCount * n == n and majorityElement == tiebreaker):
        return majorityElement
    return -1


dataSet = open("C:\\Users\\Umma\\Downloads\\input.txt", "r")

numOfArraysAndSize = [int(i) for i in dataSet.readline().split(" ")]
inputs = []
for i in range (0, numOfArraysAndSize[0]):
    inputs.append([int(i) for i in dataSet.readline().split(" ")])

dataSet.close()

majorityElements = ""
for i in range(0, numOfArraysAndSize[0]):
    majorityElements += str(FindMajorityElement(inputs[i], numOfArraysAndSize[1], None)) + " "

output = open("C:\\Users\\Umma\\Downloads\\output.txt", "a")
output.write(majorityElements)
output.close()
