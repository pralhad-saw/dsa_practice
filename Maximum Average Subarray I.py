def sumSubarray(nums,k):
     i=len(nums)
     if k<=0 or k > i:
          return 0
     max_sum= sum(nums[:k])
     cur_sum=max_sum
     for x in range(1,len(nums)-k+1):
          cur_sum = cur_sum+nums[x+k-1]-nums[x-1]
          max_sum= max(cur_sum,max_sum)
     return max_sum/k
nums=[1,0,4,5,6,7,8,9,0,3,2,1,0,4,5,7,2,9,2,1,1]
print(sumSubarray(nums,3))
# Time complexity: O(n)
# Auxiliary space: O(1) for the rolling-window logic (the initial slice temporarily uses O(k)).
