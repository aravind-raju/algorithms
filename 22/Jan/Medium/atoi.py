import sys
#Note: The value is typically 2**31 - 1 on a 32-bit platform and 2**63 - 1 on a 64-bit platform.
class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        n = len(A)
        A = A.strip()
        num = 0
        pos = True
        for i in range(len(A)):
            if i == 0 and A[i] == '+' :
                pos = True
            elif i == 0 and A[i] == '-':
                pos = False
            elif not ('0' <= A[i] <= '9'):
                return num if pos == True else (-1)*num
            else:
                num = (num) * 10 + int(A[i])
                if num > sys.maxsize and pos == True:
                    return sys.maxsize
                elif num > sys.maxsize and pos == False:
                    return -sys.maxsize - 1
                    
        return num if pos == True else (-1) * num