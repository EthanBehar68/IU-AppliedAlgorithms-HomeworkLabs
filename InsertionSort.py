array = [5, 4, 3, 2, 1, 0]
n = 6
swaps = 0

# range(start, stop, step)
for i in range(1, n):
    key = i
    while key > 0 and array[key] < array[key-1]:
        array[key], array[key-1] = array[key-1], array[key]
        swaps += 1
        key -= 1
    
print(str(array) + " and number of swaps = " + str(swaps))