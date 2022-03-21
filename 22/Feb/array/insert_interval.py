from typing import List, Dict

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #intervals.sort()
        result = []
        def dfs(i, new_start, new_end):
            if i == len(intervals):
                result.append([new_start, new_end])
                return
            start, end = intervals[i]
            if new_end < start:
                result.append([new_start, new_end])
                result.extend(intervals[i:])
                return
            if end < new_start:
                result.append(intervals[i])
                return dfs(i+1, new_start, new_end)
            return dfs(i+1, min(new_start, intervals[i][0]), max(new_end, intervals[i][1]))
        dfs(0, newInterval[0], newInterval[1])
        return result


intervals = [[3, 5], [6, 9]]
newInterval = [2, 5]
insert(intervals, newInterval)