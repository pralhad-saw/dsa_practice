def solution(text,k):
maxlen=0
maxFreq=0
left=0
count={}
for right in range(len(text)):
char=text[right]
count[char] = count.get(char,0)+1
maxFreq= max(maxFreq,count[char])
while (right-left+1) - maxFreq >k:
count[text[left]]-=1
left+=1
maxlen=max(maxlen, right-left+1)

return maxlen
# Time: O(n)
# Space: O(1
