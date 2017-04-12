# -*- coding: utf-8 -*-
#!/bin/python

import sys

n = int(raw_input().strip())

for j in range(n):
    print " " * (n - j - 1) + "#" * (j + 1)
