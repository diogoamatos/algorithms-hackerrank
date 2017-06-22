#!/bin/python
# the hurdle race
import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
height = map(int, raw_input().strip().split(' '))
# your code goes here

if max(height) > k:
    print max(height) - k
else:
    print 0

# lul
