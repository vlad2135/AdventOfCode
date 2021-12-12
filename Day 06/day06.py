import sys
import os

os.chdir(sys.path[0])
fileName = 'input'

fishTimers = []
with open(fileName, 'r') as file:
    fishTimers = [int(c) for c in file.readline().split(',')]

dayCnt = 256
fishTimersLen = len(fishTimers)

while dayCnt > 0:
    newFishCnt = 0
    for i in range(0, fishTimersLen):
        fishTimers[i] = fishTimers[i] - 1
        if (fishTimers[i]) < 0:
            fishTimers[i] = 6
            newFishCnt += 1

    if newFishCnt > 0:
        fishTimersLen += newFishCnt
        if fishTimersLen > len(fishTimers):
            fishTimers.extend([8] * len(fishTimers))

    dayCnt -= 1
    print(dayCnt)

print()
# print(len(fishTimers))
print(fishTimersLen)

