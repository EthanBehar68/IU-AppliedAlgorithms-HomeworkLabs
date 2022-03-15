#Question 1
# Original implementation was generating a 2D graph of who knew who
# but I realized I don't need that so I commented it out
# Also after the graph was completed
# I looped over whoKnowsWhoDictionary and figured out the invitees
# but I realized I can do that when I loop through r and c
# I used this these two resources to help me
# https://stepik.org/lesson/11627/step/5
# https://stackoverflow.com/questions/9966249/greedy-algorithm-implementation
def PartyPlanning(listOfPeople, pairsOfWhoKnowsWho, n):
    #peopleGraph = [['-1' for r in range(n)]for c in range(n)]
    whoKnowsWhoDictionary = {}
    invitees = []
    for r in range(n):
        person = listOfPeople[r]
        whoKnowsWhoDictionary[person] = [0, 0]
        for c in range(n):
            if r == c:
                continue
                #peopleGraph[r][c] = 'MYSELF'
            elif IKnowYou(person, listOfPeople[c], pairsOfWhoKnowsWho):
                #peopleGraph[r][c] = '1'
                whoKnowsWhoDictionary[person][0] = whoKnowsWhoDictionary[person][0]+1
            else:
                #peopleGraph[r][c] = '0'
                whoKnowsWhoDictionary[person][1] = whoKnowsWhoDictionary[person][1]+1
        if whoKnowsWhoDictionary[person][0] >= 5 and whoKnowsWhoDictionary[person][1] >= 5:
            invitees.append(person)
    return invitees

def IKnowYou(personA, personB, pairsOfWhoKnowsWho):
    doWeKnowEachOther = False
    for pair in pairsOfWhoKnowsWho:
        if personA in pair and personB in pair:
            doWeKnowEachOther = True
            break
    return doWeKnowEachOther

listOfPeople = [
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
]

pairsOfWhoKnowsWho = [
    ['A', 'B', 'J', 'K', 'L', 'U'],
    ['C', 'D', 'E', 'F', 'H', 'M'],
    ['W', 'V', 'T', 'N', 'M', 'L'],
    ['A', 'V', 'T', 'O', 'J', 'I'],
]

print(PartyPlanning(listOfPeople, pairsOfWhoKnowsWho, len(listOfPeople)))

#Question 2
# Assuming I sorted  and computed run time in method run time complexity =
# O(n * n * nlogn) O(n^3) bc you can rewrite as O(n * n * n * logn)?

# Compute runtimes and sort by shortest to longest runtime
# I assume my input is given in this arrangement(sorted shortest->longest runtime)
START_END_INDEX = 0 # index of pair of start, end times
START_INDEX = 0 # index of start time inside pair
END_INDEX = 1 # index of end time inside pair
RUNTIME_INDEX = 1 # index of runtime length
jobs = [ 
    [(13, 19), 6], #(1 P.M., 7 P.M.)-6hrs
    [(21, 4), 7], #(9 P.M., 4 A.M.)-7hrs
    [(18, 6), 10], #(6 P.M., 6 A.M.)-10hrs
    [(3, 14), 11] #(3 A.M., 2 P.M.)-11hrs
]
#A optimal answer = 13, 19 + 21, 4

jobs1 = [ 
    [(1, 2), 1], #(1 A.M., 2 A.M.)-1hrs
    [(2, 3), 1], #(2 A.M., 3 A.M.)-1hrs
    [(3, 4), 1], #(3 A.M., 4 A.M.)-1hrs
    [(4, 5), 1], #(4 A.M., 5 A.M.)-1hrs
    [(15, 16), 1] #(3 P.M., 4 P.M.)-1hrs
]
#A optimal answer = all

jobs2 = [ 
    [(23, 1), 2], #(11 P.M., 1 A.M.)-2hrs !!!
    [(24, 3), 3], #(0 A.M., 3 A.M.)-3hrs
    [(6, 12), 6], #(6 A.M., 12 P.M.)-6hrs!!!!
    [(12, 24), 12], #(12 P.M., 0 A.M.)-12hrs
    [(6, 18), 12] #(6 A.M., 6 P.M.)-12hrs
]
#A optimal answer = 23, 1 + 6, 12

jobs3 = [ 
    [(24, 1), 1],
    [(2, 3), 1], 
    [(5, 7), 2],
    [(22, 24), 2],
    [(20, 1), 5],
    [(6, 12), 6], 
    [(22, 5), 7],
    [(18, 4), 8],
    [(0, 8), 8], 
    [(12, 24), 12],
    [(6, 18), 12]
]
#A optimal answer = 24, 1 + 2, 3 + 5, 7 + 22, 24 

def Question2(jobsAndRuntimes):
    # Pick shortest run time, set to k, and add to job's
    currentJobIndex = 1
    jobLength = len(jobsAndRuntimes)
    acceptedJobs = []
    acceptedJobs.append(jobsAndRuntimes[0])

    # Is anyone's start time after k's end time?
    while currentJobIndex < jobLength:
        overlapping = True        
        for i in range(0, len(acceptedJobs)):
            acceptedJob = acceptedJobs[i]
            overlapping = IsOverlapping(acceptedJob[START_END_INDEX][START_INDEX], 
                acceptedJob[START_END_INDEX][END_INDEX], 
                jobsAndRuntimes[currentJobIndex][START_END_INDEX][START_INDEX], 
                jobsAndRuntimes[currentJobIndex][START_END_INDEX][END_INDEX])
            if overlapping:
                break

        if not overlapping:
            acceptedJobs.append(jobsAndRuntimes[currentJobIndex])

        currentJobIndex += 1

    return acceptedJobs

# I went crazy with this method.
# There is probably an easier way
# But for the life of me I can't think of it.
# Also there's probably a case or two I'm not covering
def IsOverlapping(As, Ae, Bs, Be):
    overlapping = False
    #3 - 10 = as, ae
    #1 - 4, 5 - 11, 2 - 7, 1 - 11 = bs, be
    #20 - 4, 22 - 11 = bs, be
    if As < Ae and Bs < Be:
        if (Bs <= As < Be):
            overlapping = True
        elif (As <= Bs < Ae):
            overlapping = True
        elif (As <= Bs <= Be <= Ae):
            overlapping = True
        elif (Bs <= As <= Ae <= Be):
            overlapping = True
    if As < Ae and Bs > Be:
        if (Bs <= 24) and (0 <= As < Be):
            overlapping = True
        elif (Bs <= 24) and (0 <= As <= Ae <= Be):
            overlapping = True
    #20 - 4 = as, ae
    #3 - 11, 16 - 22, 21 - 23, 23 - 1, 1 - 2, 24, 7 = bs, be
    #22 - 24, 24, 1 = as, ae
    #20, 1 = bs, be 21, 1, 2, 3
    if As > Ae and Bs < Be:
        if (0 <= Bs <= Ae):
            overlapping = True
        elif (Bs <= As < Be):
            overlapping = True
        elif (As <= Bs <= Be <= 24):
            overlapping = True
        elif (0 <= Bs <= Be <= Ae):
            overlapping = True

    if As > Ae and Bs > Be:
        if (Bs <= As <= 24) and (0 <= Ae <= Be):
            overlapping = True
        elif (As <= Bs <= 24) and (0 <= Ae <= Be):
            overlapping = True
        elif (As <= Bs <= 24) and (0 <= Be <=
         Ae):
            overlapping = True

    return overlapping

print(Question2(jobs)) #A optimal answer = 13, 19 + 21, 4
print(Question2(jobs1)) #A optimal answer = all
print(Question2(jobs2)) #A optimal answer = 23, 1 + 6, 12
print(Question2(jobs3)) #A optimal answer = 24, 1 + 2, 3 + 5, 7 + 22, 24 

# Question 3
# This was hard to wrap my head around... I think b/c n wasn't part of the problem we only had n-1 and n-3. 
# For some reason that was throwing me off.
# I had to use these resources to help me complete this problem
# https://www.engr.scu.edu/~mwang2/algorithm/Dynam10.pdf
# https://www.chegg.com/homework-help/suppose-two-teams-b-playing-match-see-first-win-n-games-part-chapter-6-problem-15-solution-9780077388492-exc
# http://cs360.cs.ua.edu/lectures/37%20Dynamic%20Programming.pdf
# http://www.cs.ucf.edu/~dmarino/progcontests/cop4516/notes/COP4516-DP2.pdf
# http://u.cs.biu.ac.il/~gelernn/83222/Lectures/Algorithms4.pdf
def WinProbability(i, j, p):
    probabilityChart = [[0.0 for Awins in range(j + 1)] for Bwins in range(i + 1)]
    probabilityChart[0][0] = 1

    for Awins in range(j+1):
        probabilityChart[0][Awins] = 1
    
    for Bwins in range(1, i+1):
        probabilityChart[Bwins][0] = 0
    
    for Awins in range(1, j+1):
        for Bwins in range(1, i+1):
            probabilityChart[Bwins][Awins] = p * probabilityChart[Bwins][Awins-1] + (1-p) * probabilityChart[Bwins-1][Awins]

    return probabilityChart[i][j]

print(WinProbability(1, 3, 0.5))

# Question 4
# This explanation helped me: https://www.youtube.com/watch?v=s6FhG--P7z0
# After understanding this - this is a really impressive algorithm.
# It's kind of fascinating to be honest.
def SubsetEqualsT(nums, t):
    subsetArray = [[False for r in range(t + 1)] for c in range (len(nums))]
    
    for r in range(len(nums)):
        subsetArray[r][0] = True

    for r in range(len(nums)):
        for c in range(1, t + 1):
            if nums[r] > c:
                subsetArray[r][c] = subsetArray[r-1][c]
            else:
                subsetArray[r][c] = subsetArray[r-1][c] or subsetArray[r-1][c - nums[r]]

    return subsetArray

def FindNumsThatEqualT(nums, subsetArray):
    c = len(subsetArray[0]) - 1
    r = len(subsetArray) - 1
    answer = []

    while not r <= 0 and not c <= 0:
        if subsetArray[r-1][c] == True:
            r = r -1
        else:
            answer.append(nums[r])
            c = c - nums[r]
            r = r -1

    # I don't know if this is necessarily correct
    if subsetArray[r][c] and not(r == 0 and c == 0):
        answer.append(nums[r])


    print(answer)

n = [4, 2, 3, 5]
t = 14
subsetArray = SubsetEqualsT(n, t)
print(subsetArray[-1][-1])
if subsetArray[-1][-1]:
    FindNumsThatEqualT(n, subsetArray)

# Question 5
# Runtime Complexity = O(nlogn) n = Length of input
# Chapter 4.1 helped me here
def DNCMaximumDifference(array):
    # Base Case
    if len(array) <= 1:
        return 0
    
    # Divide
    leftSubArray = array[:len(array)//2]
    rightSubArray = array[len(array)//2:]

    # Conquer
    leftValue = DNCMaximumDifference(leftSubArray)
    rightValue = DNCMaximumDifference(rightSubArray)

    # Check Middle
    cross = max(rightSubArray) - min(leftSubArray)

    return max(leftValue, rightValue, cross)

# Runtime Complexity = O(n) n = length of input
# Is this dynamic problem? I am not using memoization or tubalar approach.
# But I am solving the subproblem of max difference for n-1, n-2, n-3, etc
def MaximumDifference(array):
    currentMax = array[-1]
    currentDifference = array[-1] - array[-2]
    c = len(array) - 3

    while c >= 0:
        if array[c] > currentMax:
            currentMax = array[c]
            c = c -1
            continue

        if currentMax - array[c] > currentDifference:
            currentDifference = currentMax - array[c]
        c = c -1

    return currentDifference

array = [12, 9, 18, 3, 7, 11, 6, 15, 6, 1 ,10]
print(DNCMaximumDifference(array))
print(MaximumDifference(array))





