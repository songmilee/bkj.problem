import sys
import math

'''
20
25
30
6
8
---
15
'''

def main():
    l = int(sys.stdin.readline());
    a = int(sys.stdin.readline());
    b = int(sys.stdin.readline());
    c = int(sys.stdin.readline());
    d = int(sys.stdin.readline());

    total_korean = math.ceil(a / c)
    total_math = math.ceil(b / d)

    max_work_day = max(total_korean, total_math)

    print(int(l - max_work_day))

if __name__ == "__main__":
    main()
