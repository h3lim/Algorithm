from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        tmp = 0
        nums = list(sorted(set(nums)))
        left = 0
        right = 1
        if len(nums) == 0:
            return 0
        while right < len(nums):
            if nums[left] + 1 == nums[right]:
                tmp += 1
            else:
                # 1,2,3,4,100,200
                res = max(res, tmp)
                tmp = 0

            left += 1
            right += 1

        res = max(res, tmp)
        return res + 1


Solution = Solution()

res = Solution.longestConsecutive([0,1,1,2])
