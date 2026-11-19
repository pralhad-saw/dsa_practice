def findAnagrams(s,p):
  len_s, len_p = len(s), len(p)
  if len_p > len_s:
    return []
  p_count = [0] * 26
  s_count = [0] * 26
  for i in range(len_p):
    p_count[ord(p[i]) - ord('a')] += 1
    s_count[ord(s[i]) - ord('a')] += 1
  result = []
  if p_count == s_count:
    result.append(0)
  for i in range(len_p, len_s):
    s_count[ord(s[i]) - ord('a')] += 1
    left_char_index = ord(s[i - len_p]) - ord('a')
    s_count[left_char_index] -= 1
    if p_count == s_count:
      result.append(i - len_p + 1)
  return result
s = 'cbaebabacd'
p = 'abc'
print(findAnagrams(s, p))

# Time: O(n × 26) = O(n)
# Space: O(1)
