import sys
import os

os.chdir(sys.path[0])
fileName = 'input'

checkScores = {')': 3, ']': 57, '}': 1197, '>': 25137}
completeScores = {')': 1, ']': 2, '}': 3, '>': 4}
totalErrorScore = 0
openCloseMap = {'(': ')','[': ']','{': '}','<': '>'}

totalCompleteScores = []

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
                totalErrorScore += checkScores[c]
                break

        if isCorrupted:
            continue

        totalCompleteScore = 0
        chunkStack.reverse()
        for c in chunkStack:
            totalCompleteScore = totalCompleteScore * 5 + completeScores[c]
        totalCompleteScores.append(totalCompleteScore)

print(totalErrorScore)

totalCompleteScores.sort()
print(totalCompleteScores[int(len(totalCompleteScores)/2)])
