def solve(s):
  stack=[]
  #stack
  for x in s:
    if x=="#":
      if stack:
        stack.pop()
    else:
      stack.append(x)

  return stack


a = "2#ac#b"
b="#abd#"

print(solve(a)==solve(b))