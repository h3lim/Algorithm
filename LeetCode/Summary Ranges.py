class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        left = 0
        if len(nums) == 0:
            return ans
        elif len(nums) == 1:
            return [str(nums[0])]

        for right in range(len(nums) - 1):
            if nums[right + 1] == nums[right] + 1:
                continue
            else:
                if left == right:
                    ans.append(str(nums[left]))
                else:
                    ans.append(str(nums[left]) + '->' + str(nums[right]))
                left = right + 1

        if left != len(nums) - 1:
            ans.append(str(nums[left]) + '->' + str(nums[len(nums) - 1]))
        else:
            ans.append(str(nums[len(nums) - 1]))

        return ans