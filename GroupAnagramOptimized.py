
"""my solution - no ai - no copy paste not even google for syntax
we can sort each item and use that sorted item as a key for dictonary and at last just return dictionary as a lists"""

"optimize approch using alphabet tuple as key myself"
def solution(strs):
    freq = {}
    for x in strs:
      count = [0]*26
      for c in x:
        index= ord(c)-ord('a')
        count[index]+=1
      y = tuple(count)
      if y not in freq:
        freq[y]= []
      freq[y].append(x)
    return list(freq.values())
      #     y = tuple(sorted(x))
    #     if y not in freq:
    #         freq[y]= []
    #     freq[y].append(x)
    # return list(freq.values())
    
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(solution(strs))
