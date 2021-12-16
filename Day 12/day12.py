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


def getPaths(cave: str, paths: defaultdict, visited1: set, visited2: str) -> list[list]:
    totalPaths = []
    if cave == 'end':
        return [[cave]]

    if cave.islower() and cave != 'end':
        if cave in visited1 and visited2 == None:
            visited2 = cave
        else:
            visited1.add(cave)

    for nextCave in paths[cave]:
        currPath = [cave]
        if visited2 != None and nextCave in visited1:
            continue

        nextPaths = getPaths(nextCave, paths, visited1.copy(), visited2)
        if nextPaths is None or len(nextPaths) == 0:
            continue
        for nextPath in nextPaths:
            if nextPath[-1] == 'end':
                currPath.extend(nextPath)
                totalPaths.append(currPath)
                currPath = [cave]

    return totalPaths
        

visited1 = set()
visited2 = None

paths = getPaths('start', paths, visited1, visited2)
for path in paths:
    print(path)

print(len(paths))