import sys
import os

os.chdir(sys.path[0])
fileName = 'input_tst'

with open(fileName, 'r') as file:
    crabPositions = [int(c) for c in file.readline().split(',')]

crabPositions.sort()
print(crabPositions)
print(crabPositions[int(len(crabPositions)/2)-1])