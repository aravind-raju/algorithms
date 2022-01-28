import numpy as np
class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        output = []
        m = np.array(A)
        size = len(m)
        while (size > 0):
            output += list(m[0, ])
            m = np.rot90(m[1:, :])
            size = len(m)
        return output
