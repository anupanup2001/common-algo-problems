"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key= lambda x: x.start)
        i = 1

        while i < len(intervals):
            if intervals[i].start < intervals[i - 1].end:
                return False
            i += 1
        return True