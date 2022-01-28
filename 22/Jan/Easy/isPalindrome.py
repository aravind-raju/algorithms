import re
class Solution:
    def isPalindrome1(self, s: str) -> bool:
        s = re.sub('[^a-zA-Z0-9]+', '', s.lower())
        print(s)
        return True if s == s[::-1] else False
    
    def isPalindrome(self, s: str) -> bool:
        stringcheck = ''
        for letter in s:
            if letter.isalnum() == True:
                stringcheck += letter
        
        stringcheck = stringcheck.lower()
        return(stringcheck == stringcheck[::-1])
