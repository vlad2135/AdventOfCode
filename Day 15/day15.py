from collections import defaultdict
import sys
import os
import more_itertools

os.chdir(sys.path[0])
fileName = 'input'

riskMap = []
totalRiskMap = []
visitedMap = []

with open(fileName, 'r') as file:
    for line in file:
        row = [int(c) for c in line.strip()]
        riskMap.append(row)
        totalRiskMap.append([None] * len(row))
        visitedMap.append([False] * len(row))


x = 0
y = 0
totalRiskMap[y][x] = 0

def getNearestNotvisited(x,y,visitedMap):
    nvList = []
    for dx in range(-1,2):
        for dy in range(-1,2):
            if ((dx != 0 and dy != 0) or
                (y+dy < 0 or y+dy >= len(visitedMap)) or
                (x+dx < 0 or x+dx >= len(visitedMap[0])) or
                (visitedMap[y+dy][x+dx])):
                continue
            nvList.append((x+dx, y+dy))

    if len(nvList)==0:
        breakpoint()

    return nvList


while x != len(riskMap[0])-1 or y != len(riskMap)-1:
    minRiskNextY = -1
    minRiskNextX = -1

    for (nX, nY) in getNearestNotvisited(x,y,visitedMap):
        nRisk = totalRiskMap[y][x] + riskMap[nY][nX]
        if totalRiskMap[nY][nX] == None or totalRiskMap[nY][nX] > nRisk:
            totalRiskMap[nY][nX] = nRisk
        if minRiskNextX == -1:
            minRiskNextX = nX
            minRiskNextY = nY
        elif totalRiskMap[nY][nX] < totalRiskMap[minRiskNextY][minRiskNextX]:
            minRiskNextX = nX
            minRiskNextY = nY
        
    if minRiskNextX == -1:
        breakpoint()

    visitedMap[y][x] = True
    x = minRiskNextX
    y = minRiskNextY

print(totalRiskMap[9][9])
# print('\n'.join([''.join([str(cell) for cell in row]) for row in visitedMap]))
# print('\n'.join([''.join([str(cell) for cell in row]) for row in totalRiskMap]))

