#!/bin/python
# Kangaroo

import sys


x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]

jumps = 0

while True:
    jumps += 1
    x1 += v1
    x2 += v2
    if x1 == x2:
        print "YES"
        break
    elif (x2 > x1 and v2 > v1) or (x1 > x2 and v1 > v2) or (x1 != x2 and v1 == v2):
        print "NO"
        break
