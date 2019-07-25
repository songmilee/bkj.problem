import sys
from collections import deque
import heapq

MAX_VAL = 999999

vertex, edge = map(int, sys.stdin.readline().split(" "))
sp = int(sys.stdin.readline()) - 1

adj = [[] for _ in range(vertex)]
dis = [MAX_VAL for _ in range(vertex)]
dis[sp] = 0

for i in range(edge):
    u, v, w = map(int, sys.stdin.readline().split(" "))
    adj[u-1].append((v-1, w))

# 점 사이에 중복간선이 있기 때문에 priority Queue를 사용해야 함
q = []
heapq.heappush(q, (dis[sp], sp))

while q:
    dw, cur = heapq.heappop(q)
    ls = adj[cur]

    for i in ls:
        nx, cost = i
        cost += dis[cur]

        if cost > dis[nx]: continue

        if dis[nx] > cost:
            dis[nx] = cost
            heapq.heappush(q, (cost, nx))
            # q.append((next, cost))

for i in range(vertex):
    if dis[i] == MAX_VAL:
        print("INF")
    else:
        print(dis[i])