import sys
import os

os.chdir(sys.path[0])
fileName = 'input'

fishTimersInit = []
with open(fileName, 'r') as file:
    fishTimersInit = [int(c) for c in file.readline().split(',')]

dayCnt = 256
fishTimersCnt = len(fishTimersInit)

while dayCnt > 0:
    newFishCnt = 0
    for i in range(0, fishTimersCnt):
        fishTimers[i] = fishTimers[i] - 1
        if (fishTimers[i]) < 0:
            fishTimers[i] = 6
            newFishCnt += 1

    if newFishCnt > 0:
        fishTimers.extend([8] * newFishCnt)
        fishTimersCnt += newFishCnt

    dayCnt -= 1
    print(dayCnt)
    print(fishTimersCnt)

print()
print(fishTimersCnt)

