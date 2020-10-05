import sys


def solution():
    input = sys.stdin.readline()
    split_values = input.strip().split("-")

    minus_values = []

    for i in split_values:
        sum_val = 0
        plus_values = i.strip().split("+")
        for j in plus_values:
            sum_val += int(j)

        minus_values.append(sum_val)

    result = minus_values[0]
    for i in minus_values[1:]:
        result -= i

    print(result)


if __name__ == '__main__':
    solution()
