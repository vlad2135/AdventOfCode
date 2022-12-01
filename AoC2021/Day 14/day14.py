from collections import defaultdict
import sys
import os
import more_itertools

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

for i in range(0,10):
    invPoly = polymer[::-1]
    newInvPoly = ""
    for pair in more_itertools.pairwise(invPoly):
        pairStr = pair[1]+pair[0]
        newInvPoly = newInvPoly + pair[0]
        if pairStr in rules:
            newInvPoly = newInvPoly + rules[pairStr]

    newInvPoly = newInvPoly + invPoly[-1]
    
    polymer = newInvPoly[::-1]
    # print(polymer)
    
charCnt = defaultdict(int)
for c in polymer:
    charCnt[c] = charCnt[c] + 1

print(charCnt)

minOccur = min(charCnt.values())
maxOccur = max(charCnt.values())
print(minOccur, maxOccur)
print(maxOccur - minOccur)