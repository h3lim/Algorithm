from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []

        for i,h in enumerate(heights):
            if stack and stack[-1][1] > h:
                min = 0
                while stack and stack[-1][1] > h:
                    tmpI, tmpH = stack.pop()
                ans = max(ans, (i - tmpI)*tmpH)
                stack.append([tmpI, h])
            else:
                stack.append([i,h])

        while stack:
            tmpI, tmpH = stack.pop()
            tmp = (len(heights) - tmpI) * tmpH
            ans = max(ans, tmp)

Solution = Solution()

print(Solution(Solution.largestRectangleArea([2,1,5,6,2,3])))
