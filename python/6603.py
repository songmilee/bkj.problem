import sys
from itertools import combinations

def main():
    while True:
        val = sys.stdin.readline().split(" ")

        if(len(val) == 1):
            return

        k = int(val[0])
        s = [int(val[x]) for x in range(1, k + 1)]

        combi = list(combinations(s, 6))
        
        for i in combi:
            temp = list(i)
            for j in temp:
                print(j, end=' ')
            print()

        print()


if __name__ == "__main__":
    main()

'''
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0
'''