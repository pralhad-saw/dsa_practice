def solution(nums):
    totalWater=0
    for i in nums:
        leftMax=max(nums[:i])
        rightMax=max(nums[i:])
        waterLevel=min(leftMax,rightMax)
        waterAtCurrentIndex=waterLevel-height[i]
        if waterAtCurrentIndex>0:
             totalWater+=waterAtCurrentIndex
    return totalWater
