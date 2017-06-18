#!/bin/python
# Counting Valleys

import sys

def solve(n, d):
    # Complete this function
    # n -> number of steps
    # d -> steps direction
    level = 0
    valleys = 0
    aux = list(d)
    for i in range(n):
        if level == -1 and aux[i] == 'U':
            valleys += 1
        if aux[i] == 'U':
            level += 1
        elif aux[i] == 'D':
            level -= 1

    return valleys

n = int(raw_input().strip())
d = raw_input().strip()
result = solve(n, d)
print result
