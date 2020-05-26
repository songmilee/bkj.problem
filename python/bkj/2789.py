import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split(' '))
cards = [int(x) for x  in sys.stdin.readline().split(' ')]
combi = list(combinations(cards, 3))

max_val = -1
diff = 999999

for i in combi:
    val = sum(i)
    if m >= val :
        if abs(m - val) <= diff :
            diff = m - val
            max_val = val

print(max_val)