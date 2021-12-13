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

def markBasinSize(x,y, heightMap, basinMap):
    currH = heightMap[y][x]
    basinMap[y][x] = 1
    # up
    if y > 0 and heightMap[y-1][x] !=9 and heightMap[y-1][x] > currH:
        markBasinSize(x,y-1,heightMap,basinMap)
    # down
    if y < len(heightMap) - 1 and heightMap[y+1][x] !=9 and heightMap[y+1][x] > currH:
        markBasinSize(x,y+1,heightMap,basinMap)
    # left
    if x > 0 and heightMap[y][x-1] !=9 and heightMap[y][x-1] > currH:
        markBasinSize(x-1,y,heightMap,basinMap)
    # right
    if x < len(heightMap[y]) - 1 and heightMap[y][x+1] !=9 and heightMap[y][x+1] > currH:
        markBasinSize(x+1,y,heightMap,basinMap)


riskLevel = 0
basinSizes = []
for y in range(0, len(heightMap)):
    for x in range(0, len(heightMap[y])):
        if isLowPoint(x,y,heightMap):
            riskLevel+=1+heightMap[y][x]
            basinMap = [[0] * len(heightMap[yy]) for yy in range(0, len(heightMap))]
            markBasinSize(x,y,heightMap, basinMap)
            basinSize = len(list(filter(lambda n: n == 1, [i for sl in basinMap for i in sl])))
            basinSizes.append(basinSize)

print(riskLevel)

basinSizes.sort(reverse=True)
print(basinSizes[0:3])
print(basinSizes[0]*basinSizes[1]*basinSizes[2])


