import sys
import os
from collections import defaultdict

os.chdir(sys.path[0])
fileName = 'input'

paths = defaultdict(list)

with open(fileName, 'r') as file:
    for line in file:
        (cA, cB) = line.strip().split('-')
        if cA != 'end' and cB != 'start':
            paths[cA].append(cB)
        if cB != 'end' and cA != 'start':
            paths[cB].append(cA)


def getPaths2(cave: str, paths: defaultdict, alreadyVisited: set) -> list[list]:
    totalPaths = []
    if cave == 'end':
        return [[cave]]

    for nextCave in paths[cave]:
        currPath = [cave]
        if nextCave in alreadyVisited:
            continue

        if cave.islower() and cave != 'end':
            alreadyVisited.add(cave)

        nextPaths = getPaths2(nextCave, paths, alreadyVisited.copy())
        if nextPaths is None or len(nextPaths) == 0:
            continue
        for nextPath in nextPaths:
            if nextPath[-1] == 'end':
                currPath.extend(nextPath)
                totalPaths.append(currPath)
                currPath = [cave]

    return totalPaths
        

alreadyVisited = set()

paths = getPaths2('start', paths, alreadyVisited)
for path in paths:
    print(path)

print(len(paths))