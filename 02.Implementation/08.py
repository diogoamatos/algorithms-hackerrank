#!/bin/python
# Migratory Birds
import sys

n = int(raw_input().strip())
types = map(int, raw_input().strip().split(' '))
# your code goes here

highest_type = 0
highest_count = 0
for i in range(1, 6):
    aux = types.count(i)
    if highest_count < aux:
        highest_count = aux
        highest_type = i

print highest_type
