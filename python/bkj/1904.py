import sys

def main():
    n = int(sys.stdin.readline())

    a = [0] * 3

    a[0] = 1
    a[1] = 2

    for i in range(2, n):
        a[2] = (a[0] + a[1]) % 1576

        a[0] = a[1]
        a[1] = a[2]

    print(a[2])

if __name__ == "__main__":
    main()