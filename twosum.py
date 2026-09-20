def two_sum(arr,target:int):
  seen={}
  for i,n in enumerate(arr):
    required= target-n
    if required in seen:
      return [seen[required],i]
    seen[n] = i
    
  return -1


arr = [2,9,7,4,8,3,0,1,12,45,13,27,]
#num = int(input())
num= 10
print(two_sum(arr, num)
