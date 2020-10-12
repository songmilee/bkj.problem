import sys
import queue


def solution(n, m, board):
    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    que = queue.Queue()
    que.put([0, 0])

    is_visit = []
    cnt_visit = []

    for i in range(n):
        temp_1 = []
        temp_2 = []
        for j in range(m):
            temp_1.append(False)
            temp_2.append(0)

        is_visit.append(temp_1)
        cnt_visit.append(temp_2)

    cnt_visit[0][0] += 1

    while not que.empty():
        cur = que.get()

        for i in dir:
            new_x = cur[0] + i[0]
            new_y = cur[1] + i[1]

            if 0 <= new_x < n and 0 <= new_y < m:
                if not is_visit[new_x][new_y] and board[new_x][new_y] == 1:
                    cnt_visit[new_x][new_y] = cnt_visit[cur[0]][cur[1]] + 1
                    is_visit[new_x][new_y] = True
                    que.put([new_x, new_y])

    print(cnt_visit[n - 1][m - 1])


if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int, input().split(" "))
    board = []
    for _ in range(n):
        s = input().strip()
        temp = []
        for j in s:
            temp.append(int(j))

        board.append(temp)

    solution(n, m, board)
