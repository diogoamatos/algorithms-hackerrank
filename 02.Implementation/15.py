#!/bin/python
# Cats and a Mouse
import sys

arr = []

q = int(raw_input().strip())
for a0 in xrange(q):
    x, y, z, = raw_input().strip().split(' ')
    x, y, z, = [int(x), int(y), int(z)]
    if abs(x - z) == abs(y - z):
        arr.append('Mouse C')
    elif abs(x - z) > abs(y - z):
        arr.append('Cat B')
    else:
        arr.append('Cat A')

for i in range(len(arr)):
    print arr[i]
