import sys
from itertools import combinations
'''
3
..X....
.XXX...
.XX....
.....X.
.X...X.
...X...
..XX...
.XX....
.XX..X.
.X...X.
XX.....
X......
XX...XX
XXXX.XX
XXX..XX
---
1 2
'''
MAX_VALUE = 999999

def main():
    num = int(sys.stdin.readline())

    board = [[] for _ in range(num)]

    for i in range(num):
        for _ in range(5):
            board[i].append(list(sys.stdin.readline().strip()))

    cnt = MAX_VALUE
    total = list(combinations(range(num), 2))

    result = [-1, -1]

    for comb in total:
        a, b = comb
        temp_cnt = cnt_diff_board(board[a], board[b])

        # print(a, b, temp_cnt)
        if cnt > temp_cnt:
            cnt = temp_cnt
            result[0] = a
            result[1] = b

    print("{} {}".format(result[0] + 1, result[1] + 1))

def cnt_diff_board(boardA, boardB):
    cnt = 0
    for i in range(5):
        temp_zip = zip(boardA[i], boardB[i])
        cnt += sum([ 1 for j, k in temp_zip if j != k])

    return cnt

if __name__ == "__main__":
    main()