
def solution(nums):
    totalWater=0
    leftMax = [0] * len(nums)
    rightMax = [0] * len(nums)
    leftMax[0] = nums[0]
    rightMax[-1]=nums[-1]
    for i in range(1, len(nums)):
        leftMax[i] = max(leftMax[i - 1], nums[i])
    for i in range(len(nums)- 2, -1, -1):
        rightMax[i] = max(rightMax[i + 1], nums[i])
    for i in range(1,len(nums)-1):
        # leftMax=max(nums[:i+1])
        # rightMax=max(nums[i:])
        waterLevel=min(leftMax[i],rightMax[i])
        waterAtCurrentIndex=waterLevel-nums[i]
        if waterAtCurrentIndex>0:
             totalWater+=waterAtCurrentIndex
    return totalWater

# complexity
# time
# o(n)
# space
# o(n)

