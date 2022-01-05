#Problem Name: Two Characters
#Problem Link: https://www.hackerrank.com/challenges/two-characters/problem
#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def check_alternate(i, s):
    new_string = re.sub('[^{}{}]'.format(i[0], i[1]), '', s)
    print(i, s, new_string)
    if len(new_string) == 0:
        return False, new_string
    start = new_string[0]
    end = i[1] if new_string[0] == i[0] else i[0]
    alt = False
    valid = True
    for j in new_string:
        if alt:
            if j != end:
                valid = False
                break
            alt = False
        else:
            if j != start:
                valid = False
                break
            alt = True
    
    print(valid, new_string)
    return valid, new_string

def alternate(s):
    # Write your code here
    unique_char = set(s)
    if len(unique_char) == 1:
        return 0
    perm = list(permutations(unique_char, 2))
 
    # Print the obtained permutations
    max_length = 0
    for i in perm:
        status, new_string = check_alternate(i, s)
        length = len(new_string)
        if status and max_length < length:
            max_length = length
    
    return max_length
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
