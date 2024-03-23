class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        ans = [intervals[0]]

        for start, end in intervals[1:]:
            lastE = ans[-1][1]

            if start <= lastE:
                ans[-1][1] = max(lastE, end)
            else:
                ans.append([start, end])

        return ans