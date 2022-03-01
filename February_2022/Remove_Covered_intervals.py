class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda a:a[0])
        stack = []
        stack.append(intervals[0])
        for interval in intervals[1:]:
            if interval[0] >= stack[-1][0] and interval[1] <= stack[-1][1]:
                continue
            elif interval[0] == stack[-1][0] and interval[1] > stack[-1][1]:
                stack.pop()
                stack.append(interval)
            else:
                stack.append(interval)
        return len(stack)