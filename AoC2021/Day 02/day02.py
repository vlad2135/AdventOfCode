import sys
import os

os.chdir(sys.path[0])
fileName = 'input'

pos = 0
depth = 0
with open(fileName, 'r') as file:
    for line in file:
        cmdPair = line.split()
        cmd = cmdPair[0]
        cmdVal = int(cmdPair[1])
        # can't use match because of my Python being  < 3.10
        if cmd == 'forward':
            pos += cmdVal
        elif cmd == 'down':
            depth += cmdVal
        elif cmd == 'up':
            depth -= cmdVal

print("Part1. pos * depth: ", pos * depth)

pos = 0
depth = 0
aim = 0
with open(fileName, 'r') as file:
    for line in file:
        cmdPair = line.split()
        cmd = cmdPair[0]
        cmdVal = int(cmdPair[1])
        # can't use match because of my Python being  < 3.10
        if cmd == 'forward':
            pos += cmdVal
            depth += aim * cmdVal
        elif cmd == 'down':
            aim += cmdVal
        elif cmd == 'up':
            aim -= cmdVal

print("Part2. pos * depth: ", pos * depth)