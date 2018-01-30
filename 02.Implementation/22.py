#!/bin/python3
# Angry professor
import sys

def angryProfessor(k, a):
    count = 0

    for val in a:
        if val <= 0:
            count += 1
        if count >= k:
            return "NO"
    return "YES"


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        a = list(map(int, input().strip().split(' ')))
        result = angryProfessor(k, a)
        print(result)