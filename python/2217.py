import sys
from itertools import combinations

n = int(sys.stdin.readline()) # 1 ~ 100000

maxWeight = []
for i in range(n): # max value : 100000
    maxWeight.append(int(sys.stdin.readline()))

maxValue = -1
maxWeight.sort(reverse=True)

for i in range(1, n + 1):
    maxValue = max(maxValue, maxWeight[i - 1] * i)

print(maxValue)