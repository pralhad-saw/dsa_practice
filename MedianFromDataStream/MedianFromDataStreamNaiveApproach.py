#Time Complexity: O(log n) per addNum call due to heap push/pop operations; O(1)per findMedian call.
#Space Complexity: O(n) to store all n elements from the stream.

import heapq


class MedianFinder:

    def __init__(self):
        # Max-heap via negated values (smaller half)
        self.small = []
        # Min-heap (larger half)
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        # Ensure every element in small <= every element in large
        if self.small and self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Rebalance sizes so len(small) >= len(large) and diff <= 1
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0
