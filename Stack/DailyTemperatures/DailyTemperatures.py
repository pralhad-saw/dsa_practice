
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack=[] #indices or days track
        answer=[0]* len(temperatures) #answer track
        for curday,curtemp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curtemp:
                prevday = stack.pop()
                answer[prevday]= curday-prevday
            stack.append(curday)
        return answer
# time-O(N)
#space- O(N)
