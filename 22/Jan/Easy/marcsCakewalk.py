#problem link : https://www.hackerrank.com/challenges/marcs-cakewalk/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marcsCakewalk' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY calorie as parameter.
#

def marcsCakewalk(calorie, n):
    # Write your code here
    miles = 0
    i = 0
    for c in calorie:
        miles += ((2**i) * c)
        i += 1
    return miles
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(sorted(calorie, reverse=True), n)

    fptr.write(str(result) + '\n')

    fptr.close()
