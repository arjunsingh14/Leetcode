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
        intervals.sort(key=lambda x: x.start)
        res = [intervals[0]]
        for i in intervals:
            if i == 0:
                continue
            prev = res[-1]
            if i.start < prev.end:
                prev.start = min(i.start, prev.start)
                prev.end = max(i.end, prev.end)
                continue
            res.append(i)
        return len(res) == len(intervals)