"""
Question:
you are given a mxm matrix filled with alphabets. Your task is to iterate through the matrix and find all the valid words under the following constraints.

1. You can only move to the adjacent cell.
2. You can't visit a cell more than once in a word.

You are given a util method - isValidWord(string):boolean which returns true if a word is vali.d

Ex - Input
consider a 3x3 matrix

a i r
m n p
q t s

Output - air, main, pin, pint, pints, nip"""

import enchant

d = enchant.Dict("en_US")

def isValidWord(word: str) -> bool:
	return d.check(word)

def update_relative(matrix, i, j, visited_cells, valid_string):
    #Vertical movement
    if i-1 >= 0 and matrix[i-1][j] not in visited_cells:
        valid_string = check_valid_string(group_number, i-1, j, current_group)
        matrix = update_relative(matrix, i-1, j, current_group, group_number)
    if i+1 < n and matrix[i+1][j] not in visited_cells:
    	valid_string = check_valid_string(group_number, i+1, j, current_group)
        matrix = update_relative(matrix, i+1, j, current_group, group_number)
    #Horizontal movement
    if j-1 >= 0 and matrix[i][j-1] == 1:
        matrix, group_number = set_value(group_number, i, j-1, current_group)
        matrix = update_relative(matrix, i, j-1, current_group, group_number)
    if j+1 < m and matrix[i][j+1] == 1:
        matrix, group_number = set_value(group_number, i, j+1, current_group)
        matrix = update_relative(matrix, i, j+1, current_group, group_number)
    
    return matrix