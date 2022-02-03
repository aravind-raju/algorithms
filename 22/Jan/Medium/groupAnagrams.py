#link: https://leetcode.com/problems/group-anagrams/
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = {}
        for string in strs: 
            key = "".join(sorted(string))
            if lookup.get(key, None):
                lookup[key].append(string)
            else: 
                lookup[key] = [string]
                
        return list(lookup.values())