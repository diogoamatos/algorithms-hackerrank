#!/bin/python
# Utopian Tree

import sys

def get_height(n):
    height = 1
    if n == 0:
        return 1
    else:
        for i in range(n):
            if i % 2 == 0:
                height *= 2
            else:
                height += 1
    return height

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print get_height(n)
