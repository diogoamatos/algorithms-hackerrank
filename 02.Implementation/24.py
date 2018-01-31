#!/bin/python3
# Viral Advertising
import sys

def viralAdvertising(n):
    # Complete this function
    totalReach = []
    reach = 0
    for i in range(n):
        if i == 0:
            totalReach.append(2)
        else:
            totalReach.append(int((totalReach[i-1]*3)/2))
            
        reach += totalReach[i]
        
    return reach
if __name__ == "__main__":
    n = int(input().strip())
    result = viralAdvertising(n)
    print(result)
