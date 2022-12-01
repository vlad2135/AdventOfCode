import sys
import os

def calcMinFuelDay2(pos: int, crabPositions: list) -> int:
    fuel = 0
    for i in range(0, len(crabPositions)):
        moveLen = abs(crabPositions[i] - pos)
        # ugly ugly ugly solution !!
        for j in range(1, moveLen+1):
            fuel += j 

    return fuel


os.chdir(sys.path[0])
fileName = 'input'

with open(fileName, 'r') as file:
    crabPositions = [int(c) for c in file.readline().split(',')]

# crabPositions.sort()
minFuel = None
minFuelPos = None
for i in range(min(crabPositions), max(crabPositions)+1):
# for i in range(crabPositions[0], crabPositions[len(crabPositions)-1]+1):
    currMinFuel = calcMinFuelDay2(i, crabPositions)
    # print (f'For pos "{i}" fuel = {currMinFuel}')
    if minFuel == None or currMinFuel <= minFuel:
        minFuel = currMinFuel
        minFuelPos = i

print('Answer: ', minFuelPos)
print('Fuel: ', minFuel)


# print(crabPositions)
# print(crabPositions[int(len(crabPositions)/2)-1])
