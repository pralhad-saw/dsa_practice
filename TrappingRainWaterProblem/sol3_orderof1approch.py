#two pointer
#o(1) space 
def solution(nums):
    left, right = 0, len(nums) - 1
    leftMax, rightMax = 0, 0
    totalWater = 0

    while left < right:
        if nums[left] < nums[right]:
            if nums[left] >= leftMax:
                leftMax = nums[left]
            else:
                totalWater += leftMax - nums[left]
            left += 1

        else:
            if nums[right] >= rightMax:
                rightMax = nums[right]
            else:
                totalWater += rightMax - nums[right]
            right -= 1

    return totalWater
