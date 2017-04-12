# -*- coding: utf-8 -*-
#!/bin/python
# Simple Array Sun

import sys


n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

arrsum = 0
for i in arr:
    arrsum += i

print arrsum