class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            stack.append(i)

            if len(stack) > 1 and stack[-2] == '[' and stack[-1] == ']':
                stack.pop()
                stack.pop()
            if len(stack) > 1 and stack[-2] == '(' and stack[-1] == ')':
                stack.pop()
                stack.pop()
            if len(stack) > 1 and stack[-2] == '{' and stack[-1] == '}':
                stack.pop()
                stack.pop()

        if len(stack) != 0:
            return False

        return True