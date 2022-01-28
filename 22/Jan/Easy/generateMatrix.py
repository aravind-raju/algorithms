import numpy as np
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def fill_value(self, array, column, reverse, A, current_value):
        if reverse:
            for i in range(A-1, 0, -1):
                if array[column][i] == 0:
                    array[column][i] = current_value
                    current_value += 1
        else:
            for i in range(0, A-1):
                if array[column][i] == 0:
                    array[column][i] = current_value
                    current_value += 1
        return array, current_value

    def generateMatrix1(self, A):
        array = np.zeros((A, A), dtype=int)
        current_value = 1
        for _ in range(A):
            for i in range(A):
                if array[0][i] == 0:
                    array[0][i] = current_value
                    current_value += 1
            array = np.rot90(array)
        for _ in range(A):
            if array[0][0] == 1:
                break
            array = np.rot90(array)
        for i in range(1, A):
            reverse = True if i % 2 == 0 else False
            array, current_value = self.fill_value(array, i, reverse, A, current_value)
        return array
    
    def generateMatrix(self, n):
        # Initialise the matrix
        matrix = [[0] * n for _ in range(n)]
        
        # Switching direction
        switch = {'R':'D', 'D':'L', 'L':'U', 'U':'R'}

        # Next coordinate for the given direction
        nextCoord = {'R': lambda x, y: (x, y + 1), 'L': lambda x, y: (x, y - 1), \
                    'U': lambda x , y: (x - 1, y), 'D': lambda x, y: (x + 1, y)}
        
        # current direction
        currdir = 'R'
        # current coordinate
        x = y = 0
        # current value
        i = 1
        
        while i < n ** 2 + 1:
            # assign value
            matrix[x][y] = i
            
            # next coord in the same direction
            nx, ny = nextCoord[currdir](x, y)
        
            # switch direction if on the EDGE or If next coordinate is already filled
            if (y == n - 1 and currdir == 'R') or (y == 0 and currdir == 'L') \
                or (x == 0 and currdir == 'U') or (x == n - 1 and currdir == 'D') \
                or matrix[nx][ny]!=0:
                    
                currdir = switch[currdir]
            
            # next actual coordinate
            x, y = nextCoord[currdir](x, y)
            
            # increment value
            i += 1

        return matrix
            
            
            


