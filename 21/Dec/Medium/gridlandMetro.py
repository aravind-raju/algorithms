#link: https://www.hackerrank.com/challenges/gridland-metro/problem
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'gridlandMetro' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER k
#  4. 2D_INTEGER_ARRAY track
#

def gridlandMetro(n, m, k, track):
    spots = n*m
    rows = dict()

    for row in track: 
        r = row[0]
        c1 = row[1]
        c2 = row[2]
        if r not in rows:
            rows[r] = (c1, c2)
        else:
            rows[r] = (min(c1, rows[r][0]), max(c2, rows[r][1]))

    for (c1, c2) in rows.values():
        length = (c2 - c1) + 1
        spots -= length

    return spots

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    fptr.write(str(result) + '\n')

    fptr.close()
