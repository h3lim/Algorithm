from collections import deque


def solution(board):
    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visited = set()

    def bfs(i, j):
        visited.add((i, j))
        dq = deque()
        dq.append([i, j, 0])

        while dq:
            i, j, move = dq.popleft()
            if board[i][j] == "G":
                return move
            for dx, dy in dir:
                x = dx
                y = dy
                nextRow = i + dx
                nextCol = j + dy
                if nextRow < 0 or nextRow >= len(board) or nextCol < 0 or nextCol >= len(board[0]) or board[nextRow][
                    nextCol] == "D":
                    continue
                if x > 0:
                    while (i + x) < len(board) and board[i+x][j+y] != "D":
                        nextRow = i + x
                        nextCol = j + y
                        x += 1
                elif x < 0:
                    while  (i + x) >= 0 and board[i+x][j+y] != "D":
                        nextRow = i + x
                        nextCol = j + y
                        x-= 1
                elif y > 0:
                    while (j + y) < len(board[0]) and board[i+x][j+y] != "D":
                        nextRow = i + x
                        nextCol = j + y
                        y += 1
                elif y < 0:
                    while (j + y) >= 0 and board[i+x][j+y] != "D" :
                        nextRow = i + x
                        nextCol = j + y
                        y-= 1

                if (nextRow, nextCol) in visited:
                    continue

                print(nextRow, nextCol)
                visited.add((nextRow, nextCol))
                dq.append([nextRow, nextCol, move + 1])
        return -1

    ans = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "R":
                ans = bfs(i, j)

    return ans


print(solution([".D.R", "....", ".G..", "...D"]))