class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix) // 2):
            tmp = matrix[i]
            matrix[i] = matrix[len(matrix) - 1 - i]
            matrix[len(matrix) - 1 - i] = tmp

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i < j:
                    tmp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = tmp


