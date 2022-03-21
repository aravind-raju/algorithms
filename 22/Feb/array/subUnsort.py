#link: https://www.interviewbit.com/problems/maximum-unsorted-subarray/
class Solution:
	# @param A : list of integers
	# @return a list of integers
	def subUnsort(self, A):
        l = sorted(A)
        st, end = -1,-1
        for i in range(len(A)):
            if l[i] == A[i]:
                continue
            elif st == -1:
                st = i
            else:
                end = i
        if st == -1 and end == -1:
            return [-1]
        return [st ,end]
