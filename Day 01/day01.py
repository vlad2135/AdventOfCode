import sys
import os
import more_itertools

os.chdir(sys.path[0])

increaseCnt = 0
with open('input', 'r') as file:
        for pair in more_itertools.pairwise(file):
            print(pair)
            if int(pair[1]) > int(pair[0]):
                increaseCnt += 1

print(increaseCnt)
            



