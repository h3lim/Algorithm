import heapq
import queue
from collections import deque
from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 +heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
Solution = Solution()

print(Solution.leastInterval(tasks = ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"], n = 2
))
