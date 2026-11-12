
nums=[-1,0,1,2,-1,-4]
def solution(nums):
    nums.sort()
    result=[]
    for x in range(len(nums)-2):
        if x>0 and nums[x]==nums[x-1]:
            continue
        left,right = x+1, len(nums)-1
        while left<right:
            total = nums[x]+nums[left]+nums[right]
            if total==0:
                result.append([nums[x],nums[left],nums[right]])
                while left<right and nums[left]==nums[left+1]:
                    left+=1
                while left<right and nums[right]==nums[right-1]:
                    right-=1
                left+=1
                right-=1
            elif total<0:
                left+=1
            else:
                right-=1
    return result
print(solution(nums))
