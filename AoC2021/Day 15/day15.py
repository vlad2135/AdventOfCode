import sys
import os

os.chdir(sys.path[0])
fileName = 'input'

riskMap = []
totalRiskMap = []
visitedMap = []

with open(fileName, 'r') as file:
    for line in file:
        row = [int(c) for c in line.strip()]
        riskMap.append(row * 5)
        totalRiskMap.append([None] * len(row) * 5)
        visitedMap.append([False] * len(row) * 5)

origYcnt = len(riskMap)
origXcnt = origYcnt

newRiskMap = riskMap.copy()
for i in range(1, 5):
    for r in riskMap:
        newRiskMap.append(r.copy())
        totalRiskMap.append([None] * len(r))
        visitedMap.append([False] * len(r))

riskMap = newRiskMap.copy()

for y in range(0, len(riskMap)):
    for x in range(0, len(riskMap[0])):
        xIncr = x // origXcnt
        yIncr = y // origYcnt
        if xIncr == 0 and yIncr == 0:
            continue

        newRisk = (riskMap[y][x] + xIncr + yIncr) % 9
        if newRisk == 0:
            newRisk = 9

        riskMap[y][x] = newRisk

# print('\n'.join([''.join([str(cell) for cell in row]) for row in riskMap]))
x = 0
y = 0
totalRiskMap[y][x] = 0


def getNearestNotvisited(x, y, visitedMap):
    nvList = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if ((dx != 0 and dy != 0) or
                (dx == 0 and dy == 0) or
                (y+dy < 0 or y+dy >= len(visitedMap)) or
                (x+dx < 0 or x+dx >= len(visitedMap[0])) or
                (visitedMap[y+dy][x+dx])):
                continue
            nvList.append((x+dx, y+dy))

    return nvList


nextVisitQueue = []

while x != len(riskMap[0])-1 or y != len(riskMap)-1:
    nearestNotVisited = getNearestNotvisited(x, y, visitedMap)
    for (nX, nY) in nearestNotVisited:
        nRisk = totalRiskMap[y][x] + riskMap[nY][nX]
        if totalRiskMap[nY][nX] == None or totalRiskMap[nY][nX] > nRisk:
            totalRiskMap[nY][nX] = nRisk

    if len(nearestNotVisited) > 0:
        nnvGlobalRisks = [(totalRiskMap[y][x], x, y) for (x, y) in nearestNotVisited]
        nextVisitQueue.extend(nnvGlobalRisks)
        nextVisitQueue = sorted(nextVisitQueue, key=lambda t: t[0], reverse=True)

    visitedMap[y][x] = True
    while True:
        (_, x, y) = nextVisitQueue.pop()
        if not visitedMap[y][x]:
            break

    # print('next visit queue len = ', len(nextVisitQueue))
    # print('curr x=',x,' and y=',y)

print(totalRiskMap[len(riskMap)-1][len(riskMap[0])-1])
# print('\n'.join([''.join([str(cell) for cell in row]) for row in visitedMap]))
# print('\n'.join([''.join([str(cell) for cell in row]) for row in totalRiskMap]))
