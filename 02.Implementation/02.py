#!/bin/python
# Apple and Orange
import sys


s, t = raw_input().strip().split(' ')
s, t = [int(s), int(t)]
a, b = raw_input().strip().split(' ')
a, b = [int(a), int(b)]
m, n = raw_input().strip().split(' ')
m, n = [int(m), int(n)]
apple = map(int, raw_input().strip().split(' '))
orange = map(int, raw_input().strip().split(' '))

apples = 0
oranges = 0
for i in range(m):
    if s <= apple[i] + a <= t:
        apples += 1

for i in range(n):
    if s <= orange[i] + b <= t:
        oranges += 1

print apples
print oranges
