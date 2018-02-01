#!/bin/python3
# Save The Prisoner
"""
N - number of prisoners
M - number of sweets
S - prisoner ID
"""
import sys

def saveThePrisoner(n, m, s):
    # Complete this function
    poisonedId = s + m - 2
    return (poisonedId %n) + 1

t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)
