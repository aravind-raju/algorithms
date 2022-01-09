#problem-link : https://www.hackerrank.com/challenges/counter-game/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def isPowerOfTwo(x):
    # First x in the below expression
    # is for the case when x is 0
    return (x and (not(x & (x - 1))) )

def counterGame(n):
    n = bin(n)[2:]
    n = n.split('1')
    turns = len(n)+len(n[-1])-2
    return 'Louise' if turns&1 else 'Richard'

def nearestPowerOfTwo(n):
    v = n; 
    v -= 1;
    v |= v >> 1
    print(v)
    v |= v >> 2
    print(v)
    v |= v >> 4
    print(v)
    v |= v >> 8
    print(v)
    v |= v >> 16
    print(v)
    v += 1
    x = v >> 1
    print(v, n)
    return x if (v - n) > (n - x) else v
            
        
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
