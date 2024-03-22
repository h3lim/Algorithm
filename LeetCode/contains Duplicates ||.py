class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = dict()

        for i,v in enumerate(nums):
            if v in dic.keys():
                dic[v].append(i)
                dic[v].sort()
            else:
                dic[v] = [i]

        for i,l in dic.items():
            if len(l) > 1:
                for j in range(1, len(l)):
                    if abs(l[j]-l[j-1]) <= k:
                        return True


        return False