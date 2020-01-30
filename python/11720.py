import sys

def main():
    n = int(sys.stdin.readline())
    values = sys.stdin.readline()
    sum = 0
    for i in range(n):
        sum += int(values[i])

    print(sum)

if __name__ == "__main__":
    main()