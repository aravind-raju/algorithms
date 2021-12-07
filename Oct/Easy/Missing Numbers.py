#Problem Name: Missing Numbers
#Problem Link: https://www.hackerrank.com/challenges/missing-numbers/problem
#!/bin/python3

from collections import Counter
import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    # Write your code here
    c1 = Counter(arr)
    c2 = Counter(brr)
    keys = set(list(c1.keys()) + list(c2.keys()))
    output = []
    for key in keys:
        if c1.get(key, 0) != c2.get(key, 0):
            output.append(key)
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
