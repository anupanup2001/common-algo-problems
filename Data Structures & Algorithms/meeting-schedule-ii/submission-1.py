"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        maxRooms = 1
        

        intervals.sort(key  =lambda x: x.start)
        currRooms = [intervals[0].end]

        for i in range(1, len(intervals)):
            curr = intervals[i]

            if curr.start >= currRooms[0]:
                heapq.heappop(currRooms)
            heapq.heappush(currRooms, curr.end)
            maxRooms = max(len(currRooms), maxRooms)
        return maxRooms

