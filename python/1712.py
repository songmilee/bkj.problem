import sys

def main():
    a, b, c = sys.stdin.readline().split(" ")

    #string to int
    a = int(a); b = int(b); c = int(c);

    if(c == b):
        print(-1)
        return

    x = int(a / (c - b))

    if( x < 0):
        print(-1)
    else:
        print(x + 1)


if __name__ == "__main__":
    main()