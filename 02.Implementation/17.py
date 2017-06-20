#!/bin/python
# Picking number
import sys

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))


chosen = []
maxset = 0

for i in range(n):
    val = a[i]

    for j in range(n):
        if val - a[j] == 1 or  val - a[j] == 0:
            chosen.append(a[j])

    if (max(chosen) - min(chosen)) <= 1 and len(chosen) >= maxset:
        maxset = len(chosen)
        # print chosen, len(chosen)
    chosen = []

print maxset
