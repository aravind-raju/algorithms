#Link: https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate1(self, nums: List[int]) -> bool:
        seen = {}
        for i, value in enumerate(nums):
            if value in seen.keys():
                return True
            seen[value] = i
        return False
    
    def containsDuplicate(self, nums):
        return True if len(nums) > len(set(nums)) else False
        