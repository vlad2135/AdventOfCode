import sys
import os

os.chdir(sys.path[0])
fileName = 'input'

bitCount = [[0 for x in range(2)] for y in range(12)]
#bitCount = [[0 for x in range(2)] for y in range(5)]
numbers = list()
with open(fileName, 'r') as file:
    for line in file:
        digits = list(line)
        numbers.append(line)
        for i in range(0, len(digits)):
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


oxyRatingList = numbers.copy()
co2RatingList = numbers.copy()

posInNum = 0
# reinit, just to be clear
bitCount = [[0 for x in range(2)] for y in range(12)]
#bitCount = [[0 for x in range(2)] for y in range(5)]
while len(oxyRatingList) > 1:
    tmpOxy = oxyRatingList.copy()

    for number in oxyRatingList:
        bitCount[posInNum][int(number[posInNum])] += 1

    if bitCount[posInNum][0] > bitCount[posInNum][1]:
        mostCommonVal = '0'
    else:
        mostCommonVal = '1'

    oxyRatingList = list(filter(lambda s: s[posInNum] == mostCommonVal, oxyRatingList))

    posInNum += 1

# reinit, just to be clear
posInNum = 0
bitCount = [[0 for x in range(2)] for y in range(12)]
#bitCount = [[0 for x in range(2)] for y in range(5)]
while len(co2RatingList) > 1:
    tmpCo2 = co2RatingList.copy()

    for number in co2RatingList:
        bitCount[posInNum][int(number[posInNum])] += 1

    if bitCount[posInNum][0] <= bitCount[posInNum][1]:
        leastCommonVal = '0'
    else:
        leastCommonVal = '1'

    co2RatingList = list(filter(lambda s: s[posInNum] == leastCommonVal, co2RatingList))

    posInNum += 1

print('Life support rating = ', int(oxyRatingList[0], 2) * int(co2RatingList[0], 2))
