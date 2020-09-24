# https://www.acmicpc.net/problem/8958
import sys
def solution(s):
    size = len(s)
    score = [0] * size
    total = 0

    for i in range(size):
        if s[i] == 'O':
            score[i] = 1

            if i - 1 >= 0 and s[i - 1] == 'O':
                score[i] += score[i - 1]

        total += score[i]

    return total

if __name__ == "__main__":
    n = int(sys.stdin.readline())

    while n > 0:
        n -= 1
        print(solution(sys.stdin.readline()))