class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()

        for i, v in enumerate(nums):
            if v in dic.keys():
                dic[v].append(i)
            else:
                dic[v] = []
                dic[v].append(i)

        nums.sort()
        left = 0
        right = len(nums) - 1
        print(dic)
        while left < right:
            if (nums[left] + nums[right]) == target:
                if nums[left] != nums[right]:
                    return [dic[nums[left]][0], dic[nums[right]][0]]
                else:
                    return [dic[nums[left]][0], dic[nums[left]][1]]
            if nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1

