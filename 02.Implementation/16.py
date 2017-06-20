#!/bin/python
# Forming a Magic Square
import sys

s = []
for s_i in xrange(3):
    s_temp = map(int,raw_input().strip().split(' '))
    s.append(s_temp)
#  Print the minimum cost of converting 's' into a magic square

# All 3x3 magic cubes (1~9)
todosCubos = [
    [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
    [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
    [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
    [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
    [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
    [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
    [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
    [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
]

diffs = []

# TODO: zip?
for cubo in todosCubos:
    total = 0
    for cubo_row, s_row in zip(cubo, s):
        for i, j in zip(cubo_row, s_row):
            if not i == j:
                total += max([i, j]) - min([i, j])
    diffs.append(total)

print min(diffs)
