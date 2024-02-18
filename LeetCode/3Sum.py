from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            else:
                while left < right:
                    if nums[i] + nums[left] + nums[right] == 0:
                        ans.append([nums[i], nums[left], nums[right]])
                        left += 1
                        while nums[left-1] == nums[left]  and left < right:
                            left += 1
                    elif nums[i] + nums[left] + nums[right] < 0:
                        left += 1
                    else:
                        right -= 1

        return ans

solution = Solution()

ans = solution.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4])

print(ans)