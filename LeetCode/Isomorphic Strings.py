from collections import Counter


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        c1 = Counter(s)
        c2 = Counter(t)
        dic = dict()

        for i in range(len(t)):
            if c1[s[i]] != c2[t[i]]:
                return False
            if s[i] in dic.keys() and dic[s[i]] != t[i]:
                return False
            dic[s[i]] = t[i]
        return True

