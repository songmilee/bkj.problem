'''
bkj 2957
test_case
8
3
5
1
6
8
7
2
4
---
0
1
2
4
7
11
13
15
'''
import sys
from bisect import *

def main():
    test_case = int(sys.stdin.readline())

    # depth = [-1] * (test_case + 1)
    depth = {}
    sum = 0
    while test_case > 0 :
        val = int(sys.stdin.readline())
        keys = list(depth.keys())
        keys.sort()

        if len(keys) > 0 :
            upper = depth[keys[bisect_right(keys, val) - 1]]
            lower = depth[keys[bisect_left(keys, val) - 1]]
            # print(upper, lower)
            depth[val] = max(lower, upper) + 1
        else:
            depth[val] = 0

        # if upper == -1 and lower == -1:
        #     depth[val] = 0
        # else:
        #     depth[val] = max(lower, upper) + 1
        test_case -= 1

        sum += depth[val]
        print(sum)
    print(depth)


if __name__ == "__main__":
    main()