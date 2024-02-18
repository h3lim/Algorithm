class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(curr, i):
            if sum(curr) == target:
                ans.append(curr[:])

            for j in range(i, len(candidates)):
                if sum(curr) + candidates[j] <= target:
                    curr.append(candidates[j])
                    backtrack(curr, j)
                    curr.pop()

        ans = []
        backtrack([], 0)
        return ans