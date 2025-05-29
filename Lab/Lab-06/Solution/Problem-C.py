import sys
from collections import deque

def Problem_C():
    n = int(sys.stdin.readline())
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    board = [[-1]*(n+1) for i in range(n+1)]

    queue = deque()
    queue.append((x1, y1))
    board[x1][y1] = 0
    while queue:
        x, y = queue.popleft()
        moves = [(x-2, y-1), (x-2, y+1), (x+2, y-1), (x+2, y+1), (x-1, y+2), (x+1, y+2), (x-1, y-2), (x+1, y-2)]
        for i in moves:
            if 1<=i[0]<=n and 1<=i[1]<=n:
                if board[i[0]][i[1]] == -1:
                    queue.append((i[0], i[1]))
                    board[i[0]][i[1]] = board[x][y]+1

    print(board[x2][y2])


Problem_C()