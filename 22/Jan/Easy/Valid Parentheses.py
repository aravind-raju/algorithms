#link: https://leetcode.com/problems/valid-parentheses/
from collections import Counter
class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ['[', '(', '{']
        mapping = {'[':']', '(':')', '{':'}'}
        current_bracket = []
        flag = True
        for i in s:
            if i in open_brackets:
                current_bracket.append(i)
            else:
                if not current_bracket:
                    return False
                if mapping[current_bracket[-1]] != i:
                    return False
                else:
                    current_bracket.pop()
        return current_bracket == []    
