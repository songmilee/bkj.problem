import sys
from collections import deque

def main():
    r,c = map(int, sys.stdin.readline().split(' '))
    board = []

    print(board)

    for i in range(r):
        temp = sys.stdin.readline().strip()
        temp_list = []
        for j in range(c):
            temp_list.append(temp[j])

        board.append(temp_list)
    print(board)
    bfs(board, r, c)

'''
# : 울타리
. : 빈 공간
v : 늑대
k : 양
'''
def bfs(board, r, c):
    is_visit = [[False] * c for _ in range(r)]
    total_wolf = 0
    total_sheep = 0

    for i in range(r):
        for j in range(c):
            if not is_visit[i][j] and board[i][j] != "#":
                wolf, sheep = search_wolf_sheep(board, is_visit, i, j, r, c)

                total_wolf += wolf
                total_sheep += sheep

    print(total_sheep, total_wolf)


def search_wolf_sheep(board, is_visit, i, j, r, c):
    local_wolf = 0
    local_sheep = 0

    que = deque()
    que.append((i, j))

    dir = {(0, 1), (0, -1), (1, 0), (-1, 0)}

    if board[i][j] == 'v':
        local_wolf += 1
    elif board[i][j] == 'k':
        local_sheep += 1

    while que:
        cur_i, cur_j = que.pop()
        is_visit[cur_i][cur_j] = True


        for x, y in dir:
            new_i = cur_i + x
            new_j = cur_j + y

            if new_i >= 0 and new_i < r and new_j >= 0 and new_j < c:
                if not is_visit[new_i][new_j] and board[new_i][new_j] != "#":
                    que.append((new_i, new_j))
                    is_visit[new_i][new_j] = True

                    if board[new_i][new_j] == 'v':
                        local_wolf += 1
                    elif board[new_i][new_j] == 'k':
                        local_sheep += 1

    print(is_visit)
    print(local_wolf, local_sheep)
    if local_wolf >= local_sheep:
        return (local_wolf, 0)
    else:
        return(0, local_sheep)




if __name__ == "__main__":
    main()