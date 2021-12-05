import sys
import os

os.chdir(sys.path[0])
fileName = 'input'

bitCount = [[0 for x in range(2)] for y in range(12)]
with open(fileName, 'r') as file:
    for line in file:
        digits = list(line)
        for i in range(0,len(digits)-1):
            bitCount[i][int(digits[i])] += 1

gammaRateStr = ''
epsilonRateStr = ''
for pair in bitCount:
    if pair[0] > pair[1]:
        gammaRateStr += '0'
        epsilonRateStr += '1'
    elif pair[1] > pair[0]:
        gammaRateStr += '1'
        epsilonRateStr += '0'
    else:
        raise f'Equal count for {pair}'

gammaRate = int(gammaRateStr, 2)
epsilonRate = int(epsilonRateStr, 2)
print('Power consumption = ', gammaRate * epsilonRate)


