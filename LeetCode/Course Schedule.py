from typing import List
from collections import deque

from typing import List
from collections import deque

from typing import List
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a graph with an adjacency list and count of incoming edges for each node
        graph = [[] for _ in range(numCourses)]
        incoming_edges = [0] * numCourses

        # Build the graph and count the incoming edges
        for dest, src in prerequisites:
            graph[src].append(dest)
            incoming_edges[dest] += 1

        # Initialize a queue with all nodes having no incoming edges
        queue = deque([i for i in range(numCourses) if incoming_edges[i] == 0])

        # Count of courses that can be completed (used for detecting cycles)
        completed_courses = 0

        while queue:
            node = queue.popleft()
            completed_courses += 1

            # Decrease the incoming edge count for all neighbors
            for neighbor in graph[node]:
                incoming_edges[neighbor] -= 1

                # If a neighbor has no more incoming edges, add it to the queue
                if incoming_edges[neighbor] == 0:
                    queue.append(neighbor)

        # If the count of completed courses equals the total number of courses, return True
        return completed_courses == numCourses

Solution = Solution()

print(Solution.canFinish(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))

