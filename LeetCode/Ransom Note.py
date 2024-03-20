from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter1 = Counter(ransomNote)
        counter2 = Counter(magazine)

        for i in counter1.keys():
            if i not in counter2.keys():
                return False
            elif counter1[i] > counter2[i]:
                return False

        return True