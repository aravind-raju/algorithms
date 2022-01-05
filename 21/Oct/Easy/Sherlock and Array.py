#Problem Name: Sherlock and Array
#Problem Link: https://www.hackerrank.com/challenges/sherlock-and-array/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr, n):
    # Write your code here
    total = sum(arr)
    left = 0
    for i in range(n):
        total -= arr[i]
        if left == total:
            return 'YES'
        left += arr[i]
    return 'NO'

#def balancedSums(arr, n):
#    # Write your code here
#    if n == 1:
#        return 'YES'
#    else:
#        for i in range(n):
#            if i == 0:
#                left = 0
#            else:
#                left = sum(arr[:i])
#            right = sum(arr[i+1:])
#            if left == right:
#                return 'YES'
#
#    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr, n)

        fptr.write(result + '\n')

    fptr.close()
