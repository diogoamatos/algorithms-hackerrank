#!/bin/python
# Sock Merchant
import sys

def sockMerchant(n, ar):
    # Complete this function
    pairs = 0
    arraux = []
    for i in range(len(ar)):
        if ar[i] not in arraux:
            if ar.count(ar[i]) == 2:
                pairs += 1
            elif ar.count(ar[i]) > 2:
                pairs += ar.count(ar[i])/2
        arraux.append(ar[i])

    return pairs

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = sockMerchant(n, ar)
print result
