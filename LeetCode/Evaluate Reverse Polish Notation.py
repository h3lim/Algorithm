from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = 0
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        for i in tokens:
            if i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "/":
                div = stack.pop()
                stack.append(int(stack.pop() / div))
            elif i == '-':
                sub = stack.pop()
                stack.append(stack.pop() - sub)
            else:
                stack.append(int(i))

        return stack.pop()

Solution = Solution()
res = Solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print(res)