from collections import defaultdict
import sys
import os
from copy import deepcopy

os.chdir(sys.path[0])
fileName = 'input'

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

for i in range(0,40):
    newPairCnt = defaultdict(int)
    for pair in pairCnt:
        newPairCnt[pair] = pairCnt[pair]

    for pair in pairCnt:
        if not pair in rules or pairCnt[pair]<=0:
            continue

        newPair1 = pair[0]+rules[pair]
        newPair2 = rules[pair]+pair[1]

        currPairCnt = pairCnt[pair]
        newPairCnt[pair] = newPairCnt[pair] - currPairCnt
        if newPairCnt[pair] < 0:
            newPairCnt[pair] = 0

        newPairCnt[newPair1] = newPairCnt[newPair1] + currPairCnt
        newPairCnt[newPair2] = newPairCnt[newPair2] + currPairCnt

    pairCnt = newPairCnt
        

print()
# print(pairCnt)
charCnt = defaultdict(int)
for pair in pairCnt:
    if pairCnt[pair] <=0:
        continue
    charCnt[pair[0]] = charCnt[pair[0]] + pairCnt[pair]

charCnt[polymer[len(polymer)-1]] = charCnt[polymer[len(polymer)-1]] + 1
# print(charCnt)

minOccur = min(charCnt.values())
maxOccur = max(charCnt.values())
print(minOccur, maxOccur)
print(maxOccur - minOccur)