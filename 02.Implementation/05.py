#!/bin/python
# Breaking the Records
import sys


def getRecord(s):
    # Complete this function
    inc = 0
    dec = 0
    hi = s[0]
    low = s[0]
    for i in range(1, len(s)):
        if s[i] > hi:
            inc += 1
            hi = s[i]
        if s[i] < low:
            dec += 1
            low = s[i]
    return inc, dec

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
result = getRecord(s)
print " ".join(map(str, result))
