
def maxCountVowels(s:str,k:int)->int:
     vowels=set("aeiou")
     maxCount = sum(1 for char in s[:k] if char in vowels)
     cur_count =maxCount
     for x in range(k,len(s)):
          if s[x] in vowels:
               cur_count+=1
          if s[x-k] in vowels:
               cur_count-=1
          maxCount= max(cur_count,maxCount)
     return maxCount

# time-o(N)
# space-o(1)
