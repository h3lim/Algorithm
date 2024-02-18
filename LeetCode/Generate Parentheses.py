from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stack = [('(', 1, 0)]

        while stack:
            curr, left, right = stack.pop()
            if len(curr) == n * 2:
                ans.append(curr)
                continue
            if left < n:
                stack.append((curr + "(", left + 1, right))
            if right < left:
                stack.append((curr + ")", left, right + 1))

        return ans


Solution = Solution()
print(Solution.generateParenthesis(3))
