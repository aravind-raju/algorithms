from itertools import permutations
from typing import List
from collection import defaultdict

class Solution:
    def findAnagrams1(self, s: str, p: str) -> List[int]:
        length = len(p)
        string_length = len(s)
        if length > string_length: return []
        perm = permutations(p, length)
        combinations = {"".join(i):length for i in list(perm)}
        lo = 0
        hi = length
        output = []
        for i in range(string_length):
            if hi > string_length:
                break
            value = s[lo:hi]
            if combinations.get(value, None):
                output.append(lo)
            lo +=1
            hi +=1
        return output
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hm, res, pL, sL = defaultdict(int), [], len(p), len(s)
        if pL > sL: return []

        # build hashmap
        for ch in p: hm[ch] += 1

        # initial full pass over the window
        for i in range(pL-1):
            if s[i] in hm: hm[s[i]] -= 1
            
        # slide the window with stride 1
        for i in range(-1, sL-pL+1):
            if i > -1 and s[i] in hm:
                hm[s[i]] += 1
            if i+pL < sL and s[i+pL] in hm: 
                hm[s[i+pL]] -= 1
                
            # check whether we encountered an anagram
            if all(v == 0 for v in hm.values()): 
                res.append(i+1)
                
        return res