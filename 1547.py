import sys

def main():
    cups = [1, 2, 3]

    n = int(sys.stdin.readline())
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split(" "))

        #index를 뽑음
        index_x = cups.index(x)
        index_y = cups.index(y)

        #값을 변경
        temp = cups[index_x]
        cups[index_x] = cups[index_y]
        cups[index_y] = temp
    
    print(cups[0])

        



if __name__ == "__main__":
    main()

'''
4
3 1
2 3
3 1
3 2
'''