def solution(nums):
 prefix[0] = 1
 suffix[len(nums)-1] = 1
 result=[0]*len(nums)
 prefix[0]=nums[0]
 suffix[len(nums)-1]=nums[len(nums)-1]
 for i in range(1,len(nums)):
  prefix[i] = nums[i-1] * prefix[i-1]
  suffix[len(nums)-1-i] = nums[len(nums)-i] * suffix[len(nums)-i]
 for i in range(len(nums)):
  result[i]=prefix[i]*suffix[i]
 return result

# Time: O(n)
# Auxiliary space: O(n)
