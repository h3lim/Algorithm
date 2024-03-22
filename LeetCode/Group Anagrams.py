class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        dic = dict()
        l = list()
        sortedW = set()

        for i in strs:
            tmp = list(i)
            tmp.sort()
            s = "".join(tmp)
            sortedW.add(s)
            l.append(s)

        for i in sortedW:
            dic[i] = []

        for i in range(len(l)):
            dic[l[i]].append(strs[i])

        for i in dic.values():
            ans.append(i)

        return ans
