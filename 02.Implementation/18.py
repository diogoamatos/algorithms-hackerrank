#!/bin/python
# Climbing the leaderboard

n = int(raw_input().strip())
scores = map(int,raw_input().strip().split(' '))
m = int(raw_input().strip())
alice = map(int,raw_input().strip().split(' '))
# your code goes here

rank = []
for i in scores:
    if i not in rank:
        rank.append(i)

pos = len(rank)
# aux = []

for nota in alice:
    tmp = 0
    position = 0

    for i in range(pos-1, -1, -1):
        if nota <= rank[i]:
            if nota == rank[i]:
                # aux.append(i+1)
                position = i+1
            else:
                # aux.append(i+2)
                position = i+2
            tmp = i+1
            break

        if nota > rank[i] and i == 0:
            tmp = i+1
            # aux.append(tmp)
            position = i+1

    pos = tmp
    print position

# Nao esta passando pelos testes 6, 7, 8 e 9 devido a timeout
# Nao sei como
