def solution(nums):
    prefix_sum =[]
    sum=0
    for x in nums:
         sum=sum+x
         prefix_sum.append(sum)
         
    return prefix_sum
nums = [3, 2, 5, 1, 6]
