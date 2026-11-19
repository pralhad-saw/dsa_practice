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
 remainderCount={}
 prefixsum=0
 for i in range(len(nums)):
  prefixsum+= nums[i]
  rem = prefixsum%k
  if remainderCount.get(rem):
   if i-remainderCount>=2: return True
  else:
   remainderCount[rem]=i
 return False
