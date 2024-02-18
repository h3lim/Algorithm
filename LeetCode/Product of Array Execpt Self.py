from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        prod = 1
        d = dict()

        for i in nums:
            if i != 0:
                prod = prod * i
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] = d[i] + 1

        for i in range(len(nums)):
            if 0 in nums and d[0] > 1:
                ans.append(0)
            elif 0 in nums and d[0] == 1:
                if nums[i] != 0:
                    ans.append(0)
                else:
                    ans.append(prod)
            else:
                ans.append(prod // i)

        return ans

Solution = Solution()
ans = Solution.productExceptSelf([1,2,3,4])
