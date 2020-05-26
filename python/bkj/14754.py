import sys


def main():
    n, m = map(int, sys.stdin.readline().split(' '))

    sum_val = 0
    view = []

    pizza = []

    for _ in range(n):
        ls = [int(x) for x in sys.stdin.readline().split(' ')]
        sum_val += sum(ls)
        pizza.append(ls)

        val = max(ls)
        if val not in view:
            view.append(val)

    for i in range(m):
        ls = [pizza[x][i] for x in range(n)]
        val = max(ls)

        if val not in view:
            view.append(val)

    sum_view_val = sum(view)
    sum_val -= sum_view_val

    print(sum_val)

if __name__ == "__main__":
    main()