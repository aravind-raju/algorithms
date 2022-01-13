#link: https://www.hackerrank.com/challenges/beautiful-pairs/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY A
#  2. INTEGER_ARRAY B
#
def beautifulPairs(A, B, n):
    X=[]
    #slicing creates a copy of the array
    for i in A[::-1]:
        print(i)
        if i in B:
            A.remove(i)
            B.remove(i)
            X.append(i)
            print(len(A), len(B))
    return n-1 if len(X)==n else len(X)+1
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B, n)

    fptr.write(str(result) + '\n')

    fptr.close()
