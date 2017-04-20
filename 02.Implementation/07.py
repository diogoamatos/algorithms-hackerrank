#!/bin/python
import sys

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
a = map(int, raw_input().strip().split(' '))
# write your code here

counter = 0
for i in range(n):
    for j in range(i+1, n):
        aux = a[i] + a[j]
        if (aux) % k == 0 and i < j:
            counter += 1

print counter