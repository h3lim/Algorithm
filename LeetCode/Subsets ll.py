class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, i):
            if i > len(nums):
                return

            if sorted(curr) not in ans:
                tmp = sorted(curr)
                ans.append(tmp[:])

            for j in range(i, len(nums)):
                curr.append(nums[j])
                backtrack(curr, j + 1)
                curr.pop()
        
        ans = []
        backtrack([], 0)
        return ans