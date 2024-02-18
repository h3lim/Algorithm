from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        l = [[p, s] for p, s in zip(position, speed)]

        l = sorted(l, reverse=True)

        for p, s in l:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()

        return len(stack)


