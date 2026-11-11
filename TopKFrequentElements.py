"""
5th challenge: Top K Frequent Elements.

This is a useful step toward harder Google-style DSA problems because it introduces frequency counting and efficient selection.

Given:
nums = [1, 1, 1, 2, 2, 3]
k = 2


nums = [1, 1, 1, 2, 2, 3]
k = 2
Return the k most frequent elements.

Expected output: [1, 2]

Think about how you can reuse the frequency dictionary you already know."""
def solution(nums,k):
  freq ={}
  for x in nums:
    freq[x]= freq.get(x,0)+1
  values = sorted(freq.items(),key = lambda x:x[1],reverse=True)
  return [x[0] for x in values[:k]]
print(solution(nums,k))


Complexity:
- Time: O(n + m log m)
- Space: O(m)
