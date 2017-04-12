#!/bin/python

import sys


a, b, c, d, e = raw_input().strip().split(' ')
a, b, c, d, e = [int(a), int(b), int(c), int(d), int(e)]

sum1 = b + c + d + e
sum2 = a + c + d + e
sum3 = a + b + d + e
sum4 = a + b + c + e
sum5 = a + b + c + d

print min(sum1, sum2, sum3, sum4, sum5), max(sum1, sum2, sum3, sum4, sum5)
