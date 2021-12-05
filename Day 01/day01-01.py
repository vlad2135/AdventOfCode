import sys
import os

os.chdir(sys.path[0])

increaseCnt = 0
prev = None
with open('input', 'r') as file:
        prev = int(file.readline())
        for line in file:
            curr = int(line)
            if curr > prev:
                increaseCnt += 1
            prev = curr

print(increaseCnt)
            



