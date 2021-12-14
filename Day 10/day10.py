
import sys
import os

os.chdir(sys.path[0])
fileName = 'input'

prizeScores = {')': 3, ']': 57, '}': 1197, '>': 25137}
totalErrorScore = 0
openCloseMap = {'(': ')','[': ']','{': '}','<': '>'}


with open(fileName, 'r') as file:
    for line in file:
        chunkStack = []
        isCorrupted = False
        for c in line.strip():
            if c in ['(','[','{','<']:
                chunkStack.append(openCloseMap[c])
            else:
                if len(chunkStack) == 0:
                    isCorrupted = True
                else:
                    lastOpener = chunkStack.pop()
                    if lastOpener != c:
                        isCorrupted = True

            if isCorrupted == True:
                totalErrorScore += prizeScores[c]
                break

print(totalErrorScore)


