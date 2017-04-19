#!/bin/python
# Birthday Chocolate
import sys


def getWays(squares, d, m):
    # Complete this function
    counter = 0
    if len(squares) <= 1:
        if squares[0] == d:
            counter += 1
        return counter

    for i in range(len(squares)-m+1):
        squares_sum = 0
        for j in range(m):
            squares_sum += squares[i+j]
            if squares_sum == d and j == m-1:
                counter += 1

    return counter


n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = raw_input().strip().split(' ')
d, m = [int(d), int(m)]
result = getWays(s, d, m)
print(result)
