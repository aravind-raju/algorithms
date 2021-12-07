#Problem Name: Mars Exploration
#Problem Link: https://www.hackerrank.com/challenges/mars-exploration/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    message = 'SOS'
    j = 0
    count = 0
    for i in s:
        print(message[j], i, j)
        if message[j] != i:
            count += 1
        
        j += 1
        if j == 3:
            j = 0
    
    return count
    #return sum(1 for i in range(len(s)) if s[i]!="SOS"[i%3])
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()