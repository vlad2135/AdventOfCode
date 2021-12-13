import sys
import os

os.chdir(sys.path[0])
fileName = 'input'

heightMap = []
with open(fileName, 'r') as file:
    for line in file:
        row = [int(c) for c in line.strip()]
        heightMap.append(row)

def isLowPoint(x, y, heightMap):
    currPnt = heightMap[y][x]
    ltu = y == 0 or currPnt < heightMap[y-1][x]
    ltd = y == len(heightMap)-1 or currPnt < heightMap[y+1][x]
    ltl = x == 0 or currPnt < heightMap[y][x-1]
    ltr = x == len(heightMap[y])-1 or currPnt < heightMap[y][x+1]
    return ltu and ltd and ltl and ltr


riskLevel = 0
for y in range(0, len(heightMap)):
    for x in range(0, len(heightMap[y])):
        if isLowPoint(x,y,heightMap):
            riskLevel+=1+heightMap[y][x]


print(riskLevel)