#!/bin/python
import sys

def bonAppetit(n, k, b, ar):
    #Complete this function
    charge = 0
    for i in range(n):
        if i != k:
            charge += ar[i]
    charge = charge/2
    if b == charge:
        return "Bon Appetit"
    return b - charge


n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
b = int(raw_input().strip())
result = bonAppetit(n, k, b, ar)
print result
