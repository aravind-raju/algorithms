#Problem Name: Sum vs XOR
#Problem Link: https://www.hackerrank.com/challenges/sum-vs-xor/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def sumXor(n):
    # You can see that XOR behaves exactly like addition except in one case when A=1 and B=1.
    #Knowing this you can find out when  x+n = x^n will be true. If for any i, the ith bit of x and n are both 1, we have to take care of the carry bit when adding the number and the equation won't be true.
    #If the ith bit of x is 1, n must have a 1 in its 1th bit. Otherwise the bit in n can be either 0 or 1. Take the binary representation of x and count the number of zeros, ignoring leading zeros. If the number of zeros in the binary is b, the answer is 2^^b.
    
    #count = 0
    #for x in range(n+1):
    #    if n + x == n ^ x:
    #        count += 1
    
    #return count
    return 2**(bin(n).count('0')-1)-bool(not n)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
