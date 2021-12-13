import sys
import os

def calcMinFuel(pos: int, crabPositions: list) -> int:
    fuel = 0
    for i in range(0, len(crabPositions)):
        fuel += abs(crabPositions[i] - pos)

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
    currMinFuel = calcMinFuel(i, crabPositions)
    print (f'For pos "{i}" fuel = {currMinFuel}')
    if minFuel == None or currMinFuel <= minFuel:
        minFuel = currMinFuel
        minFuelPos = i

print('Answer: ', minFuelPos)
print('Fuel: ', minFuel)


# print(crabPositions)
# print(crabPositions[int(len(crabPositions)/2)-1])
