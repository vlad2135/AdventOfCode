import sys
import os

os.chdir(sys.path[0])
fileName = 'input'

#seaMap = [[0 for x in range(10)] for y in range(10)]
seaMap = [[0 for x in range(1000)] for y in range(1000)]

with open(fileName, 'r') as file:
    for line in file:
        (coord1, coord2) = line.split(' -> ')
        (x1, y1) = [int(n) for n in coord1.split(',')]
        (x2, y2) = [int(n) for n in coord2.split(',')]

        if x1 != x2 and y1 != y2:
            continue

        if (x1 == x2):
           for y in range(min(y1, y2), max(y1, y2)+1):
               seaMap[y][x1]+= 1 
        else:
           for x in range(min(x1, x2), max(x1, x2)+1):
               seaMap[y1][x]+= 1 

mostDangerous = 0
for y in range(0, len(seaMap)):
    for x in range(0, len(seaMap[0])):
        if seaMap[y][x] > 1:
            mostDangerous+= 1

print(mostDangerous)