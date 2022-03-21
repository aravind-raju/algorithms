class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqDict, windowStart = {},0  # freqDict is our frequency hashMap
        maxRepeatCount, maxLength = 0, 0
        
        for windowEnd, rightChar in enumerate(s):
            # inserting our chars into the hashMap
            if rightChar in freqDict:
                freqDict[rightChar] += 1
            else:
                freqDict[rightChar] = 1
            
            # Calculating the maxRepeatCount
            # We should use the frequency of the current letter to get
            # the number of times its being repeated
            maxRepeatCount = max(maxRepeatCount, freqDict[rightChar])
            
            
            # Shrinking the window if our replacements if greater than k
            while windowEnd - windowStart + 1 - maxRepeatCount > k:
                leftChar = s[windowStart]
                # Decreasing the frequency of the char that is going out of our window
                if leftChar in freqDict:
                    freqDict[leftChar] -= 1
                windowStart += 1
            maxLength = max(maxLength, windowEnd - windowStart + 1)
        return maxLength