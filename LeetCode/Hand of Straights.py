from typing import List
import heapq
"""class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        if len(hand) % groupSize != 0:
            return False

        l = []
        i = 0

        while len(hand) != 0:
            if len(l) != 0:
                if l[len(l) - 1] + 1 in hand:
                    elmt = l[len(l) - 1] + 1
                    l.append(elmt)
                    hand.remove(elmt)
                else:
                    return False
            else:
                l.append(hand[i])
                hand.remove(hand[i])

            if len(l) == groupSize:
                l = list()
        return True
"""
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n,0)

        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]

            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True


Solution = Solution()

print(Solution.isNStraightHand([1,2,3,6,2,3,4,7,8],3))
