import sys

def main():
    n = int(sys.stdin.readline())

    time = [int(x) for x in sys.stdin.readline().split(' ')]

    time.sort()
    total_time = []

    sum = 0
    for i in range(n):
        if i == 0:
            total_time.append(time[i])
            sum += total_time[i]

        else:
            total_time.append(time[i] + total_time[i-1])
            sum += total_time[i]

    print(sum)

if __name__ == "__main__":
    main()