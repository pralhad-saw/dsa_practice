class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        n = len(self.nums)
        mid = n // 2

        if n % 2 == 1:
            return float(self.nums[mid])
        return (self.nums[mid - 1] + self.nums[mid]) / 2.0


""" Time Complexity: O(1) for addNum, and O(nlog n) for every findMedian call. Across \(n\) operations, this reaches 

O(n^2 log n), which triggers a Time Limit Exceeded (TLE) on LeetCode's larger test cases.


Space Complexity: O(n) to hold all stream elements in memory.

"""