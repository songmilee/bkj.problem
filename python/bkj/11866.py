import sys

def main():
    n, k = map(int, sys.stdin.readline().split(" "))

    list = []

    for i in range(n):
        list.append((i + 1))

    cnt = 1
    index = 0
    print("<", end='')

    while len(list) > 0:
        size = len(list)

        if cnt == k:
            if index >= size:
                index = 0
            val = list.pop(index)

            if len(list) > 0:
                print(val, end=', ')
            else:
                print(val, end='>')
            cnt = 1
            continue

        index = index + 1
        if index > size:
            index = 0
            continue
        cnt = cnt + 1



if __name__ == "__main__":
    main()