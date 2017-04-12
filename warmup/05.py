#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int, raw_input().strip().split(' '))
    a.append(a_temp)

primary = 0

for i in range(n):
    primary += a[i][i]

secondary = 0
for i in range(n):
    secondary += a[i][n-1-i]

print abs(primary - secondary)
