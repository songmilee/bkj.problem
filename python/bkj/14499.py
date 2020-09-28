import sys

# 1 = east 2 = west  3= north 4= south

def solution(board, x, y, move_order):
    dice_col = [0, 0, 0, 0]
    dice_row = [0, 0, 0]

    n = len(board)
    m = len(board[0])

    move = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    new_row = y
    new_col = x

    for i in move_order:
        i = i - 1

        move_row = move[i][1] + new_row
        move_col = move[i][0] + new_col

        # 범위 검사
        if 0 <= move_row < m and 0 <= move_col < n:
            new_row = move_row
            new_col = move_col

            #north
            if i == 2:
                # 주사위 세로 방향 이동(아래)
                first_col = dice_col[0]
                for i in range(3):
                    dice_col[i] = dice_col[i + 1]
                dice_col[-1] = first_col

                dice_row[1] = dice_col[1]

            #south
            elif i == 3:
                # 주사위 세로로 이동(위)
                last_col = dice_col[-1]
                for i in range(3, 0, -1):
                    dice_col[i] = dice_col[i - 1]
                dice_col[0] = last_col

                dice_row[1] = dice_col[1]

            #east
            elif i == 0:
                #주사위 가로 방향 (오른쪽)
                last_row = dice_row[-1]
                for i in range(2, 0, -1):
                    dice_row[i] = dice_row[i - 1]
                dice_row[0] = dice_col[-1]
                dice_col[-1] = last_row

                dice_col[1] = dice_row[1]

            #west
            else:
                #주사위 가로 방향 (왼쪽)
                first_row = dice_row[0]
                for i in range(2):
                    dice_row[i] = dice_row[i + 1]
                dice_row[-1] = dice_col[-1]
                dice_col[-1] = first_row

                dice_col[1] = dice_row[1]

            #마지막 값 업데이트
            if board[new_col][new_row] == 0:
                board[new_col][new_row] = dice_col[-1]
            else:
                dice_col[-1] = board[new_col][new_row]
                board[new_col][new_row] = 0

            print(dice_col[1])





if __name__ == '__main__':
    input = sys.stdin.readline

    n, m, x, y, k = map(int, input().split(" "))

    board = []

    for _ in range(n):
        board.append(list(map(int, input().split(" "))))

    move_order = list(map(int, input().split(" ")))
    solution(board, x, y, move_order)

