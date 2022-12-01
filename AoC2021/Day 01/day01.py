import sys
import os
import more_itertools

os.chdir(sys.path[0])
fileName = 'input'

increaseCnt = 0
with open(fileName, 'r') as file:
    for pair in more_itertools.pairwise(file):
        if int(pair[1]) > int(pair[0]):
            increaseCnt += 1

print("Tuple increase count: ", increaseCnt)

prevTripleSum = None
increaseCntTriple = 0
with open(fileName, 'r') as file:
    for triple in more_itertools.triplewise(file):
        sum = int(triple[0])+int(triple[1])+int(triple[2])
        if prevTripleSum is not None and sum > prevTripleSum:
            increaseCntTriple += 1
        prevTripleSum = sum

print("Triple increase count: ", increaseCntTriple)