import sys
import os

os.chdir(sys.path[0])
fileName = 'input_tst'

#bitCount = [[0 for x in range(2)] for y in range(12)]
bitCount = [[0 for x in range(2)] for y in range(5)]
numbers = list()
with open(fileName, 'r') as file:
    for line in file:
        digits = list(line)
        numbers.append(line)
        for i in range(0, len(digits)-1):
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


def filterByPosValue(s: str, pos: int, val: str) -> bool:
    return s[pos] == val


oxyRatingList = numbers.copy()
co2RatingList = numbers.copy()

posInNum = 0
while len(oxyRatingList) > 1 or len(co2RatingList) > 1:
    tmpOxy = oxyRatingList.copy()
    tmpCo2 = co2RatingList.copy()
    if (len(oxyRatingList)) > 1:
        oxyRatingList = list(filter(lambda s: filterByPosValue(s, posInNum, gammaRateStr[posInNum]), oxyRatingList))

    if (len(co2RatingList)) > 1:
        co2RatingList = list(filter(lambda s: filterByPosValue(s, posInNum, epsilonRateStr[posInNum]), co2RatingList))
    
    if (len(oxyRatingList)) < 1:
        breakpoint()

    if (len(co2RatingList)) < 1:
        breakpoint()

    posInNum += 1

print('Life support rating = ', int(oxyRatingList[0], 2) * int(co2RatingList[0], 2))


