#Problem Name: majority-element
#Problem Link: https://www.interviewbit.com/problems/majority-element/

from collections import Counter
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        count = Counter(A)
        return count.most_common(1)[0][0]