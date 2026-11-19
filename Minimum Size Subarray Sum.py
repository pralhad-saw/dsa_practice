def solution(nums,target):
left=0
currentSum=0
minLen=float('inf')
for right in range(len(nums)):
currentSum+=nums[right]
while currentSum>=target:
minLen= min(minLen,right-left+1)
currentSum-=nums[left]
left+=1
return minLen if minLen != float('inf') else 0
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))
