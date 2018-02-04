# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.sort(key=lambda x: x.start)
        return all(f.end <= s.start for f,s in zip(intervals, intervals[1:]))
        # for f, s in zip(intervals, intervals[1:]):
        #     if f.end > s.start:
        #         return False
        # return True
