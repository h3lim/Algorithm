from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, i):
            if i > len(nums):
                return

            ans.append(curr[:])

            for j in range(i, len(nums)):
                curr.append(nums[j])
                backtrack(curr, j + 1)
                curr.pop()

        ans = []
        backtrack([], 0)
        return ans


Solution = Solution()

print(Solution.subsets([1,2,3]))


