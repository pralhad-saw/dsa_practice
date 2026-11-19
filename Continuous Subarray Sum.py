# Brute force 
def solution(nums,k):
 for i in (len(nums)-1):
  count=nums[i]
 for j in (i+1 ,len(nums)):
  count+= nums[j]
 if count % k ==0:
  return True
 return False


# prefix sum 
def solution(nums,k):
 remainderCount = {0: -1}
 prefixsum=0
 for i in range(len(nums)):
  prefixsum+= nums[i]
  # rem = prefixsum%k
  # edge case for k=0
  if k != 0:
    rem = prefixsum % k
  else:
    rem = prefixsum
  if rem in remainderCount:
   if i - remainderCount[rem] >= 2: return True
  else:
   remainderCount[rem]=i
 return False
nums = [23, 2, 4, 6, 7]
k = 6
