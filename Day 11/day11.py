import sys
import os
import pdb

os.chdir(sys.path[0])
fileName = 'input'

cavern = []
with open(fileName, 'r') as file:
    for line in file:
        cavern.append([])
        for c in line.strip():
            cavern[len(cavern)-1].append(int(c))


def increaseAround(x: int, y: int, cavern: list):
    if x-1 >= 0 and y-1 >=0:
        cavern[y-1][x-1] = cavern[y-1][x-1] + 1
    if y-1 >=0:
        cavern[y-1][x] = cavern[y-1][x] + 1
    if x+1 < len(cavern[y]) and y-1 >=0:
        cavern[y-1][x+1] = cavern[y-1][x+1] + 1

    if x-1 >= 0:
        cavern[y][x-1] = cavern[y][x-1] + 1
    if x+1 < len(cavern[y]):
        cavern[y][x+1] = cavern[y][x+1] + 1

    if x-1 >= 0 and y+1 < len(cavern):
        cavern[y+1][x-1] = cavern[y+1][x-1] + 1
    if y+1 < len(cavern):
        cavern[y+1][x] = cavern[y+1][x] + 1
    if x+1 < len(cavern[y]) and y+1 < len(cavern):
        cavern[y+1][x+1] = cavern[y+1][x+1] + 1


def flashAndCount(cavern: list, alreadyFlashed: list) -> int: 
    flashCnt = 0
    for y in range(0, len(cavern)):
        for x in range(0, len(cavern[y])):
            if alreadyFlashed[y][x] == 1:
                continue

            if cavern[y][x] > 9:
                alreadyFlashed[y][x] = 1
                flashCnt += 1
                increaseAround(x,y,cavern)

    anotherFlashCnt = 0
    if flashCnt > 0:
        anotherFlashCnt = flashAndCount(cavern, alreadyFlashed)
    
    return flashCnt + anotherFlashCnt


totalFlashCnt = 0

alreadyFlashed = [[0] * len(cavern[yy]) for yy in range(0, len(cavern))]
i = 0
while True:

    for y in range(0, len(cavern)):
        for x in range(0, len(cavern[y])):
            cavern[y][x] = cavern[y][x] + 1
    
    totalFlashCnt += flashAndCount(cavern, alreadyFlashed)
    # print('step ', i)
    # print('alreadyFlashed:')
    # print('\n'.join([''.join([str(cell) for cell in row]) for row in alreadyFlashed]))

    stepFlashCnt = 0
    for y in range(0, len(cavern)):
        for x in range(0, len(cavern[y])):
            if alreadyFlashed[y][x] == 1:
                cavern[y][x] = 0
                stepFlashCnt+=1
                alreadyFlashed[y][x] = 0

    if stepFlashCnt == len(cavern) * len(cavern[0]):
        print('first step for all flash = ', i+1)
        exit()

    # print('cavern:')
    # print('\n'.join([''.join([str(cell) for cell in row]) for row in cavern]))
    i+=1

print(totalFlashCnt)

