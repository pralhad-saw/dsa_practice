def solution(nums):
  result=0
  left = 0
  right = len(nums) - 1
  while left<right:
    amount = (right-left)* min(nums[left],nums[right])
    if nums[left]<nums[right]:
      left+=1
    else:
      right-=1
    if amount>result:
      result = amount
    
nums=[1,2,4,1,3,7,8,2,9,4]
solution(nums)
# #complexity analysis
# time-o(n)
# space-o(1)
