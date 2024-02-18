import queue
import math
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        pq = queue.PriorityQueue()

        for point in points:
            distance = (point[0] ** 2 + point[1] ** 2)
            pq.put((distance, point))

        for _ in range(k):
            n, point = pq.get()
            ans.append(point)

        return ans