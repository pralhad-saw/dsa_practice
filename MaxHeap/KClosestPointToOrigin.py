import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        if not points or k<=0:
            return []
        maxheap=[]
        for x,y in points:
            dist = x**2 + y**2
            heapq.heappush(maxheap, (-dist,x,y))

            if len(maxheap)>k:
                heapq.heappop(maxheap)
        return [[x,y] for _,x,y in maxheap]
