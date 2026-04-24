class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort() # sort by start time

        ans = []
        i = 1
        n = len(intervals)
        ans.append(intervals[0])
        while i < n:
            curr_interval = intervals[i]
            prev_interval = ans[-1]
            if curr_interval[0] <= prev_interval[1]:
                # Merge
                ans[-1] = ([min(curr_interval[0], prev_interval[0]), max(curr_interval[1], prev_interval[1])])
            else:
                ans.append(curr_interval)
            i = i + 1
        return ans
