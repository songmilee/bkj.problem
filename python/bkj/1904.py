import sys

def solution():
    n = int(sys.stdin.readline())
    dp = [0] * 3

    dp[0] = 1
    dp[1] = 2

    if n < 3:
        print(n)
        return

    for _ in range(2, n):        
        dp[2] = (dp[0] + dp[1]) % 15746

        dp[0] = dp[1]
        dp[1] = dp[2]
    
    print(dp[2])

if __name__ == "__main__":
    solution()