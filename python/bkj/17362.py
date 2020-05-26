import sys

n = int(sys.stdin.readline())

if n <= 5:
    print(n)
elif (n -1) % 8 == 0:
    print(1)
elif (n-3) % 4 == 0:
    print(3)
elif (n-5) % 8 == 0:
    print(5)
elif (n + 6) % 8 == 0:
    print(2)
elif n % 8 == 0:
    print(2)
else:
    print(4)