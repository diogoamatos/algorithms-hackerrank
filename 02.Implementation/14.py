#!/bin/python
# Electronics Shop

def getMoneySpent(keyboards, drives, s):
    # Complete this function
    totalValue = 0

    # TODO: how to reduce complexity
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            aux = keyboards[i] + drives[j]
            if aux <= s and totalValue < aux:
                totalValue = aux

    if totalValue == 0:
        return -1

    return totalValue

s, n, m = raw_input().strip().split(' ')
s, n, m = [int(s), int(n), int(m)]
keyboards = map(int, raw_input().strip().split(' '))
drives = map(int, raw_input().strip().split(' '))

moneySpent = getMoneySpent(keyboards, drives, s)
print moneySpent
