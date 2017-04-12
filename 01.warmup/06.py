# -*- coding: utf-8 -*-
# Plus Minus
#!/bin/python

import sys

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))


negs = 0
pos = 0
zeros = 0
for i in range(n):
    if arr[i] < 0:
        negs += 1
    elif arr[i] > 0:
        pos += 1
    else:
        zeros += 1

print float(pos)/n
print float(negs)/n
print float(zeros)/n
