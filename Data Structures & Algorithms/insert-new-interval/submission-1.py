class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        i = 0

        while i < len(intervals) and intervals[i][0] < newInterval[0]:
            ans.append(intervals[i])
            i = i + 1
        
        # Add new interval
        if ans and newInterval[0] <= ans[-1][1]:
            # Merge
            ans[-1][1] = max(ans[-1][1], newInterval[1])
        else:
            ans.append(newInterval)

        print (ans)
        # merge remaining if needed
        while i < len(intervals):
            last_interval = ans[-1]
            curr_interval = intervals[i]

            if curr_interval[0] <= last_interval[1]:
                last_interval[1] = max(curr_interval[1], last_interval[1])
            else:
                # There is no overlap
                ans.append(intervals[i])
            i = i + 1
        
        return ans
