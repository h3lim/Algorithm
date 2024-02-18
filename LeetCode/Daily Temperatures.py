from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                stackIdx, stackTemp = stack.pop()
                ans[stackIdx] = i - stackIdx
            stack.append([i, t])

        return ans

Solution = Solution()
print(Solution.dailyTemperatures([73,74,75,71,69,72,76,73]))
