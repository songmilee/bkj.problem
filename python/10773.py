import sys

def main():
    stack = []
    k = int(sys.stdin.readline())
    sum_stack = 0

    while k > 0 :
        value = int(sys.stdin.readline())

        if value != 0:
            stack.append(value)
        else:
            stack.pop()
        k = k - 1

    sum_stack = sum(stack)
    print(sum_stack)

if __name__ == "__main__":
    main()