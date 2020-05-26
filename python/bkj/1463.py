import sys

n = int(sys.stdin.readline())
cnt = [1000001] * (n + 1)
cnt[n] = 0

while n > 1:
    if n % 3 == 0:
        temp = int(n/3)
        cnt[temp] = min(cnt[temp], cnt[n] + 1)

    if n % 2 == 0:
        temp = int(n/2)
        cnt[temp] = min(cnt[temp], cnt[n] + 1)

    temp = n - 1
    cnt[temp] = min(cnt[temp], cnt[n] + 1)

    n = n - 1

print(cnt[1])

