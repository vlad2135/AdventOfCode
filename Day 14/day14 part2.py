from collections import defaultdict
import sys
import os
from copy import deepcopy

os.chdir(sys.path[0])
fileName = 'input_tst'

rules = {}

with open(fileName, 'r') as file:
    polymer = file.readline().strip()
    file.readline()

    for line in file:
        line = line.strip()
        (cond, result) = line.split(' -> ')
        rules[cond] = result

print(polymer)
print(rules)

pairCnt = defaultdict(int)
for i in range(0,len(polymer)-1):
    pairStr = polymer[i]+polymer[i+1]
    pairCnt[pairStr] = pairCnt[pairStr] + 1 

print(pairCnt)

for i in range(0,1):
    newPairCnt = defaultdict(int)
    newPairCnt = deepcopy(pairCnt)
    for pair in pairCnt:
        if not pair in rules:
            continue

        newPair1 = pair[0]+rules[pair]
        newPair2 = rules[pair]+pair[1]
        newPairCnt[pair] = pairCnt[pair] - 1
        if newPairCnt[pair] <= 0:
            newPairCnt.pop(pair)

        if newPair1 in pairCnt:
            newPairCnt[newPair1] = pairCnt[newPair1] + 1
        else:
            newPairCnt[newPair1] = 1

        if newPair2 in pairCnt:
            newPairCnt[newPair2] = pairCnt[newPair2] + 1
        else:
            newPairCnt[newPair2] = 1

    pairCnt = newPairCnt
        

print()
print(pairCnt)
charCnt = defaultdict(int)
for pair in pairCnt:
    charCnt[pair[0]] = charCnt[pair[0]] + pairCnt[pair]
    charCnt[pair[1]] = charCnt[pair[1]] + pairCnt[pair]

print(charCnt)

minOccur = min(charCnt.values())
maxOccur = max(charCnt.values())
print(minOccur, maxOccur)
print(maxOccur - minOccur)