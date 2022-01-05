#Problem Name: Connected Cells in a Grid
#Problem Link: https://www.hackerrank.com/challenges/connected-cell-in-a-grid/copy-from/240991985
#!/bin/python3

import math
import os
import random
import re
import sys
import itertools
from collections import Counter

#
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#
def update_relative(matrix, i, j, current_group, group_number):
    #Vertical movement
    if i-1 >= 0 and matrix[i-1][j] == 1:
        matrix, group_number = set_value(group_number, i-1, j, current_group)
        matrix = update_relative(matrix, i-1, j, current_group, group_number)
    if i+1 < n and matrix[i+1][j] == 1:
        matrix, group_number = set_value(group_number, i+1, j, current_group)
        matrix = update_relative(matrix, i+1, j, current_group, group_number)
    #Horizontal movement
    if j-1 >= 0 and matrix[i][j-1] == 1:
        matrix, group_number = set_value(group_number, i, j-1, current_group)
        matrix = update_relative(matrix, i, j-1, current_group, group_number)
    if j+1 < m and matrix[i][j+1] == 1:
        matrix, group_number = set_value(group_number, i, j+1, current_group)
        matrix = update_relative(matrix, i, j+1, current_group, group_number)
    #Diagonal movement
    if i-1 >=0 and j-1 >= 0 and matrix[i-1][j-1] == 1:
        matrix, group_number = set_value(group_number, i-1, j-1, current_group)
        matrix = update_relative(matrix, i-1, j-1, current_group, group_number)
    if i+1 < n and j+1 < m and matrix[i+1][j+1] == 1:
        matrix, group_number = set_value(group_number, i+1, j+1, current_group)
        matrix = update_relative(matrix, i+1, j+1, current_group, group_number)
    if i-1 >=0 and j+1 < m and matrix[i-1][j+1] == 1:
        matrix, group_number = set_value(group_number, i-1, j+1, current_group)
        matrix = update_relative(matrix, i-1, j+1, current_group, group_number)
    if i+1 < n and j-1 >= 0 and matrix[i+1][j-1] == 1:
        matrix, group_number = set_value(group_number, i+1, j-1, current_group)
        matrix = update_relative(matrix, i+1, j-1, current_group, group_number)
    
    return matrix


def set_value(group_number, i, j, current_group):
    if current_group:
        matrix[i][j] = current_group
    else:
        group_number += 1
        matrix[i][j] = 'x' + str(group_number)
    
    return [matrix, group_number]

def connectedCell(matrix, n, m):
    # Write your code here
    current_group = None
    group_number = 1
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 0:
                if matrix[i][j] == 1:
                    matrix, group_number = set_value(group_number, i, j, current_group)

                if matrix[i][j] not in [0, 1]:
                    current_group = matrix[i][j]
                else:
                    current_group = None
                
                #Vertical movement
                if i-1 >= 0 and matrix[i-1][j] == 1:
                    matrix, group_number = set_value(group_number, i-1, j, current_group)
                    matrix = update_relative(matrix, i-1, j, current_group, group_number)
                if i+1 < n and matrix[i+1][j] == 1:
                    #print(i, j, current_group)
                    matrix, group_number = set_value(group_number, i+1, j, current_group)
                    matrix = update_relative(matrix, i+1, j, current_group, group_number)
                #Horizontal movement
                if j-1 >= 0 and matrix[i][j-1] == 1:
                    matrix, group_number = set_value(group_number, i, j-1, current_group)
                    matrix = update_relative(matrix, i, j-1, current_group, group_number)
                if j+1 < m and matrix[i][j+1] == 1:
                    matrix, group_number = set_value(group_number, i, j+1, current_group)
                    matrix = update_relative(matrix, i, j+1, current_group, group_number)
                #Diagonal movement
                if i-1 >=0 and j-1 >= 0 and matrix[i-1][j-1] == 1:
                    matrix, group_number = set_value(group_number, i-1, j-1, current_group)
                    matrix = update_relative(matrix, i-1, j-1, current_group, group_number)
                if i+1 < n and j+1 < m and matrix[i+1][j+1] == 1:
                    matrix, group_number = set_value(group_number, i+1, j+1, current_group)
                    matrix = update_relative(matrix, i+1, j+1, current_group, group_number)
                if i-1 >=0 and j+1 < m and matrix[i-1][j+1] == 1:
                    matrix, group_number = set_value(group_number, i-1, j+1, current_group)
                    matrix = update_relative(matrix, i-1, j+1, current_group, group_number)
                if i+1 < n and j-1 >= 0 and matrix[i+1][j-1] == 1:
                    matrix, group_number = set_value(group_number, i+1, j-1, current_group)
                    matrix = update_relative(matrix, i+1, j-1, current_group, group_number)
                current_group = None
    
    #[print(i) for i in matrix]
    totals = Counter(i for i in list(itertools.chain.from_iterable(matrix)))
    del totals[0]
    #print(totals.most_common(2))
    return totals.most_common(1)[0][1]
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix, n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
