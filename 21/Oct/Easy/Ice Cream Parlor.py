#Problem Name: Ice Cream Parlor
#Problem Link: https://www.hackerrank.com/challenges/icecream-parlor/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr, n):
    # Write your code here
    for i in range(n):
        diff = m - arr[i]
        if diff in arr[i + 1:n]:
            li1 = arr[i + 1:n] 
            x = li1.index(diff)
            return [i + 1, i + x + 2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr, n)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
