#!/bin/python
# Between two sets
"""
1. All elements in A are factors of x.
2 x is a factor of all elements in B.
"""


n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
a = map(int, raw_input().strip().split(' '))
b = map(int, raw_input().strip().split(' '))


def mmc(x, vetor):
    for valor in vetor:
        if valor % x:
            return False
    return True


def mmc_selector(x, vetor):
    selected = []
    for valor in vetor:
        if valor >= x and valor % x == 0 and valor not in selected:
            selected.append(valor)
    return selected

x = []

for i in range(1, min(b)+1):
    if mmc(i, b) and i not in x:
        x.append(i)

for i in a:
    x = mmc_selector(i, x)

print len(x)
