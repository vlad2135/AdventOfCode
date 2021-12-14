import sys
import os
from collections import defaultdict

os.chdir(sys.path[0])
fileName = 'input_tst'

paths = defaultdict(list)

with open(fileName, 'r') as file:
    for line in file:
        (cA, cB) = line.strip().split('-')
        if cA != 'end' and cB != 'start':
            paths[cA].append(cB)
        if cB != 'end' and cA != 'start':
            paths[cB].append(cA)


def getPaths(cave, paths, alreadyVisited):
    # implement generator here
    for nextCave in paths[cave]:
        if nextCave in alreadyVisited:
            continue

        if nextCave=='end':
            yield cave+','+nextCave
        else:
            if cave.islower():
                alreadyVisited.add(cave)

            for nextPath in getPaths(nextCave, paths, alreadyVisited):
                yield cave+','+nextPath

    yield 'end'


alreadyVisited = set()

for path in sorted(getPaths('start', paths, alreadyVisited)):
    print(path)



