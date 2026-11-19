# O(n) time
# O(1) auxiliary space

def solution(nums,k):
zeroCount=0
left=0
maxlen=0
for right in range(len(nums)):
if nums[right]==0:
zeroCount+=1
while zeroCount>k:
if nums[left]==0:
zeroCount-=1
left+=1
maxlen=max(maxlen,right-left+1)
return maxlen
