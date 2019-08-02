import sys

def main():
    n = int(sys.stdin.readline())

    fib = [0] * (n + 1)

    fib[0] = 0
    fib[1] = 1

    cnt = 2

    while cnt <= n:
        fib[cnt] = fib[cnt - 1] + fib[cnt - 2]
        cnt = cnt + 1

    print(fib[n])

if __name__ == "__main__":
    main()

