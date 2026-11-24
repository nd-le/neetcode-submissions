"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTimes = sorted([i.start for i in intervals])
        endTimes = sorted([i.end for i in intervals])
        i, j = 0, 0
        count = 0
        ans = 0

        while i < len(startTimes):
            if startTimes[i] < endTimes[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1

            ans = max(ans, count)

        return ans
