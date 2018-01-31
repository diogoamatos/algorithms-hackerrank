#!/bin/python3
# Beautiful Days at the Movies
import sys

def beautifulDays(i, j, k):
    # Complete this function
    
    count = 0
    for day in range(i, j+1):
        number = day
        inv = 0
        while number > 0:
            rest = number%10
            inv = (inv*10) + rest
            number = number//10

        if (abs(day-inv)/k)%1 == 0:
            count +=1

    return count

if __name__ == "__main__":
    i, j, k = input().strip().split(' ')
    i, j, k = [int(i), int(j), int(k)]
    result = beautifulDays(i, j, k)
    print(result)
