
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack=[]
        max_area=0
        n=len(heights)
        for i in range(n+1):
            current_height = heights[i] if i<n else 0
            while stack and current_height < height[stack[-1]]:
                height = heights[stack.pop()]
                left_boundary = stack[-1] if stack else -1
                width = i - 1 - left_boundary
                max_area = max(max_area, height*width)
            stack.append(i)
        return max_area
