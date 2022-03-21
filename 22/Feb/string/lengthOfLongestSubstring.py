class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        unq = {}
        max_length = 0
        current_length = 0
        for i in s:
            if unq.get(i, None) is None:
                unq[i] = 1
                current_length += 1
            else:
                current_length = 0
                unq = {}
            max_length = max(max_length, current_length)
        return max_length
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        non_rep_sub_str = ""
        for i in s:
            if i in non_rep_sub_str:
                non_rep_sub_str = non_rep_sub_str.split(i)[1] + i
            else:
                non_rep_sub_str += i
                max_length = max(max_length, len(non_rep_sub_str))
        return max_length
            