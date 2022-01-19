#https://www.hackerrank.com/challenges/jim-and-the-orders/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jimOrders' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY orders as parameter.
#

def jimOrders0(orders):
    # Write your code here
    prep_time = []
    for i, j in orders:
        prep_time.append(i+j)
    time = sorted(prep_time)
    output = []
    count = 0
    for i in time:
        index = prep_time.index(i)+1
        if index in output:
            del prep_time[index-1]
            count +=1
        output.append(index + count)
    return output

def jimOrders(orders):
    s = sorted(enumerate(orders, 1), key=lambda x:sum(x[1]))
    #print(s) --> [(1, [1, 3]), (2, [2, 3]), (3, [3, 3])]
    return [i[0] for i in s]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
