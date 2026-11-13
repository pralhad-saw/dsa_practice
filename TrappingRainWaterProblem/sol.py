
def solution(nums):
    totalWater=0
    for i in range(1,len(nums)-1):
        leftMax=max(nums[:i+1])
        rightMax=max(nums[i:])
        waterLevel=min(leftMax,rightMax)
        waterAtCurrentIndex=waterLevel-nums[i]
        if waterAtCurrentIndex>0:
             totalWater+=waterAtCurrentIndex
    return totalWater

#  complexity
# time
# o(n2)
