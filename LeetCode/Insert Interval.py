class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        intervals.append(newInterval)
        intervals.sort(key=lambda i: i[0])
        ans.append(intervals[0])

        for start, end in intervals[1:]:
            lastE = ans[-1][1]

            if start <= lastE:
                ans[-1][1] = max(lastE, end)
            else:
                ans.append([start, end])

        return ans