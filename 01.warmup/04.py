# -*- coding: utf-8 -*-
#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

arrsum = 0

for i in range(n):
    arrsum += arr[i]

print arrsum
