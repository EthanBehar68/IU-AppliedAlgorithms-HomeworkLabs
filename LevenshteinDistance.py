# Solve the subproblem - how many edits do we need for the substrings
def LevenshteinDistance(string1, string2):
    # Create 2D array like such:
    # Creates our base cases for first row and first column
    # The rest isn't important at this point.
    # 0, 1, 2, 3, 4, 5 ... -> string1
    # 1, 1, 2, 3, 4, 5
    # 2, 1, 2, 3, 4, 5
    # 3, 1, 2, 3, 4, 5,
    # 4, 1, 2, 3, 4, 5,
    # ... -> string2

    distanceArray = [[r for r in range(len(string1) + 1)] for c in range (len(string2) + 1)]
    for c in range(1, len(string2) + 1):
        distanceArray[c][0] = distanceArray[c-1][0] + 1

    for c in range(1, len(string2)+1):
        for r in range(1, len(string1)+1):
            # -1 b/c we added an empty space in distanceArray 
            # when building arrays with the +1
            if string2[c-1] == string1[r-1]:
                distanceArray[c][r] = distanceArray[c-1][r-1]
            else:
                distanceArray[c][r] = 1 + min(distanceArray[c-1][r], distanceArray[c][r-1], distanceArray[c-1][r-1])
    return distanceArray[-1][-1]

dataSet = open("C:\\Users\\Umma\\Downloads\\input.txt", "r")

string1 = dataSet.readline()
string2 = dataSet.readline()

dataSet.close()

answer = LevenshteinDistance(string1, string2)
print(answer)

output = open("C:\\Users\\Umma\\Downloads\\output.txt", "a")
output.write(str(answer))
output.close()