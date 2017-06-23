#!/bin/python
# Designer PDF viwer

import sys


h = map(int, raw_input().strip().split(' '))
word = raw_input().strip()

letters_height = {
    'a': h[0],
    'b': h[1],
    'c': h[2],
    'd': h[3],
    'e': h[4],
    'f': h[5],
    'g': h[6],
    'h': h[7],
    'i': h[8],
    'j': h[9],
    'k': h[10],
    'l': h[11],
    'm': h[12],
    'n': h[13],
    'o': h[14],
    'p': h[15],
    'q': h[16],
    'r': h[17],
    's': h[18],
    't': h[19],
    'u': h[20],
    'v': h[21],
    'w': h[22],
    'x': h[23],
    'y': h[24],
    'z': h[25],
}
max_height = 0
for i in list(word):
    if letters_height[i] > max_height:
        max_height = letters_height[i]

print len(word) * max_height
