class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda i: i[0])
        newPoints = [points[0]]

        for start, end in points[1:]:
            lastE = newPoints[-1][1]

            if start <= lastE:
                newPoints[-1][1] = min(lastE, end)
            else:
                newPoints.append([start, end])

        return len(newPoints)
