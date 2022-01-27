#link: https://leetcode.com/problems/product-of-array-except-self/
import numpy

class Solution:
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        output = []
        for i, value in enumerate(nums):
            temp = nums.copy()
            del temp[i]
            output.append(numpy.prod(temp))
        return output
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        result = [1]*N
        
        curr = 1
        for i in range(N):
            if i != 0:
                result[i] *= curr
            curr *= nums[i]
        
        curr = 1
        for i in range(N-1, -1, -1):
            if i != N-1:
                result[i] *= curr
            curr *= nums[i]
        
        return result
        