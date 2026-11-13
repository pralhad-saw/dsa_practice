def rangesum(nums,s,e):
    prefix_sum =[]
    sum=0
    for x in nums:
         sum=sum+x
         prefix_sum.append(sum)
     if s==0:
         return  prefix_sum[e]
    return prefix_sum[e]-prefix_sum[s-1]
nums = [3, 2, 5, 1, 6]
start=1
end=3
print(rangesum(nums,start,end))
