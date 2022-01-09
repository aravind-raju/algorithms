#link: https://www.hackerrank.com/challenges/luck-balance/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def get_number_imp_contest(contests):
    count = 0
    for i in contests:
        if i[1] == 1:
            count +=1
    return count

def luckBalance_1(k, contests):
    # Write your code here
    sorted_contests = sorted(contests)
    print(k, sorted_contests)
    loss_count = get_number_imp_contest(sorted_contests) - k
    print(loss_count)
    luck = 0
    for i in sorted_contests:
        if loss_count == 0:
            luck += i[0]
            print("loss count 0", luck)
        else:
            if i[1] == 0:
                luck += i[0]
                print("new luck", luck)
            else:
                loss_count -= 1
                luck -= i[0]
                print("In else")
    return luck

def luckBalance(k, contests):
    important, optional = [], 0
    for x, y in contests:
        if y: 
            important.append(x)
        else: 
            optional += x
    if k < len(important):
        s = sorted(important)
        i = len(s)-k
        return optional + sum(s[i:]) - sum(s[:i])
    return optional + sum(important)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
