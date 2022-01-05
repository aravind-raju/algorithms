#Problem Name: Super Reduced String
#Problem Link: https://www.hackerrank.com/challenges/reduced-string/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    i = 0
    flag = True
    while(flag):
        l = len(s)
        if i+1 >= l:
            break
        if s[i] == s[i+1]:
            if len(s) == 2:
                flag = False
                s = ''
            else:
                s = s[0:i] + s[i+2:]
                i = -1
        i += 1
    if len(s) == 0:
        return 'Empty String'
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
