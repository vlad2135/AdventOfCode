from collections import defaultdict
import sys
import os

os.chdir(sys.path[0])
fileName = 'input'

fishTimers = []
with open(fileName, 'r') as file:
    fishTimers = [int(c) for c in file.readline().split(',')]

ftDict = defaultdict(int)
maxTv = 8
for ft in fishTimers:
    ftDict[ft] = ftDict[ft] + 1

dayCnt = 256

while dayCnt > 0:
    for i in range(0, maxTv+1):
        ftDict[i-1] = ftDict[i]

    ftDict[6] = ftDict[6]+ftDict[-1]
    ftDict[8] = ftDict[-1]
    dayCnt-=1

ftDict[-1] = 0

print(sum(ftDict.values()))
