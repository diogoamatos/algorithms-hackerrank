#!/bin/python

import sys

n = int(raw_input().strip())
height = map(int, raw_input().strip().split(' '))

max_height = 0
counter = 0

max_height = height[0]

for i in range(n):
    if max_height < height[i]:
        max_height = height[i]
        counter = 1
    elif max_height == height[i]:
        counter += 1

print counter
