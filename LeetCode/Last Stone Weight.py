import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for item in stones:
            heapq.heappush(max_heap, -item)

        while len(max_heap) > 1:
            largest1 = -heapq.heappop(max_heap)
            largest2 = -heapq.heappop(max_heap)

            if largest1 == largest2:
                continue
            else:
                heapq.heappush(max_heap, -(largest1 - largest2))

        if len(max_heap) == 1:
            return -heapq.heappop(max_heap)
        else:
            return 0