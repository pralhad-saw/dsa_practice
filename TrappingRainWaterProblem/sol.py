
def solution(nums):
  wateramount = 0
  left=nums[0]
  for right in range(1,len(nums)):
    if ((right - left) <2) or nums[right]==0 or nums[right]<nums[right-1]:
      continue
    if nums[left] ==0:
      left+=1
    amount = min(nums[left],nums[right]) * (right-left)
    wateramount+=amount
  return wateramount
