class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        num = n

        while num != 1:
            digits = [int(digit) for digit in str(num)]
            num = sum([sq ** 2 for sq in digits])
            if num in s:
                return False
            else:
                s.add(num)

        return True