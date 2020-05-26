'''
from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
a = [[] for _ in range(n+1)]
check = [False for _ in range(n+1)]
ans = []
hacking = 0

def bfs(i):
    global hacking
    q = deque()
    q.append(i)
    check[i] = True
    cnt = 0
    while q:
        x = q.popleft()
        for k in a[x]:
            if check[k] is False:
                q.append(k)
                check[k] = True
                cnt += 1
    if hacking < cnt:
        hacking = cnt
        ans.clear()
        ans.append(i)
    elif hacking == cnt:
        ans.append(i)

for _ in range(m):
    u, v = map(int, input().split())
    a[v].append(u)
for i in range(1, n+1):
    check = [False for _ in range(n+1)]
    bfs(i)
ans.sort()
for i in ans:
    print(i, end=' ')
print()
'''
import sys
from collections import deque

def bfs(vertex, graph):

    q = deque()
    is_visit = [False] * n

    q.append(vertex)
    cnt = 0

    while q:
        cnt += 1

        cur = q.popleft()
        is_visit[cur] = True

        for j in graph[cur]:
            if not is_visit[j]:
                q.append(j)

    return cnt

#get input
n, m = map(int, sys.stdin.readline().split(' '))

# 메모리를 줄이기 위해 2차원 행렬 대신 갈 수 있는 배열을 만듦
graph = [[] for _ in range(n)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split(" "))
    graph[y - 1].append(x - 1)


vertex_list = []
max_cnt = -1
for i in range(n):
    cnt = bfs(i, graph)
    if cnt > max_cnt:
        vertex_list = [i + 1]
        max_cnt = cnt
    elif cnt == max_cnt:
        vertex_list.append(i + 1)

vertex_list.sort()
for i in vertex_list:
    print(i, end=' ')
print()
