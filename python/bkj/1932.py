# 1932.py
'''
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
'''
import sys
def main():
    n = int(sys.stdin.readline())
    triangle = [[] for _ in range(n)]
    dp = [[-1] *(i+1) for i in range(n)]

    for i in range(n):
        temp = sys.stdin.readline().split(" ")
        for j in temp:
            triangle[i].append(int(j))

    dp[0] = triangle[0]

    maxValue = -1
    for i in range(1, n):
        size = len(triangle[i])
        for j in range(size):
            if j != size - 1:
                dp[i][j] = max(dp[i][j], triangle[i][j] + dp[i-1][j])

            if j + 1 < size:
                dp[i][j+1] = max(dp[i][j+1], triangle[i][j + 1] + dp[i-1][j])
        maxValue = max(dp[i])

    print(maxValue)

if __name__ == "__main__":
    main()