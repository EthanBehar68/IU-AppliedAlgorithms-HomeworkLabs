# Greey Algorithm
# NOT OPTIMAL!
# def minNumberOfCointsForChangeGreedy(moneyTarget, coins):
#     numberOfCoins = 0
#     c = len(coins) - 1
#     while c >= 0:
#         largestCoin = coins[c]
#         if largestCoin <= moneyTarget:
#             moneyTarget -= largestCoin
#             numberOfCoins += 1
#         else:
#             c -= 1        
#     # Couldn't make exact change
#     if moneyTarget != 0:
#         return -1
#     else:
#         return numberOfCoins

def minNumberOfCointsForChange(moneyTarget, coins):
    numsToTarget = [float("inf")] * (moneyTarget + 1)
    numsToTarget[0] = 0
    for c in range (len(coins)):
        coin = coins[c]
        for n in range (len(numsToTarget)):
            if coin <= n:
                numsToTarget[n] = min(numsToTarget[n], 1 + numsToTarget[n - coin])
    
    if numsToTarget[moneyTarget] != float("inf"):
        return numsToTarget[moneyTarget]
    # Couldn't make exact change.
    else:
        return -1
        
dataSet = open("C:\\Users\\Umma\\Downloads\\input.txt", "r")

moneyTarget = int(dataSet.readline())
coins = [int(i) for i in dataSet.readline().split(',')]

dataSet.close()

answer = minNumberOfCointsForChange(moneyTarget, coins)
print(answer)

output = open("C:\\Users\\Umma\\Downloads\\output.txt", "a")
output.write(str(answer))
output.close()