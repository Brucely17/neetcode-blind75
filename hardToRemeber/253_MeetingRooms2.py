
intervals = [[0,30],[5,10],[15,20]]
from typing import (
    List,
)
from lintcode import (
    Interval,
)
import heapq

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        intervals.sort(key=lambda x:x.start)

        heap=[]
        heapq.heappush(heap,intervals[0].end)

        for i in range(1,len(intervals)):
            if heap[0]<=intervals[i].start:
                heapq.heappop(heap)
            heapq.heappush(heap,intervals[i].end)
        
        return len(heap)
        
