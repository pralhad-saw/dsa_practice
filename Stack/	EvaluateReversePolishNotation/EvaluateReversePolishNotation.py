
from typing import List
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack=[0]
        for token in tokens:
            if token == '+':
                stack.append(stack.pop()+stack.pop())
            elif token =='-':
                b,a=stack.pop(),stack.pop()
                stack.append(a-b)
            elif token =='/':
                b,a=stack.pop(),stack.pop()
                stack.append(int(a/b))
            elif token=='*':
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(token))
        return stack[0]
