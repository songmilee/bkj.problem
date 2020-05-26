'''
from heapq import *
input=__import__('sys').stdin.readline
for __ in range(int(input())):
    n,d,c=map(int,input().split())
    S=[float('inf')]*(n+1)
    D=[[] for _ in range(n+1)]
    for i in range(d):
        a,b,s=map(int,input().split())
        D[b].append((a,s))
    q=[];heappush(q,(0,c));S[c]=0
    while q:
        t,x=heappop(q)
        if S[x]!=t:continue
        for nx,nt in D[x]:
            if S[nx]>nt+t:
                S[nx]=nt+t;heappush(q,(nt+t,nx))
    ans=0;Max=0
    for i in range(1,n+1):
        if S[i]!=float('inf'):
            ans+=1;Max=max(Max,S[i])
    print(ans,Max)
'''
import sys
import heapq

test_case = int(sys.stdin.readline())
MAX_VAL = 999999
while test_case > 0:
    n, d, c = [int(x) for x in sys.stdin.readline().split()]
    adj = [[] for _ in range(n)]
    is_visit = [False] * n
    dis = [MAX_VAL] * n
    dis[c - 1] = 0

    for _ in range(d):
        a, b, s = [int(x) for x in sys.stdin.readline().split()]
        adj[b-1].append((a-1, s))

    q = []
    heapq.heappush(q, (dis[c-1], c-1))
    cnt = 0
    max_time = -1
    while q:
        cost, cur = heapq.heappop(q)
        ls = adj[cur]

        if is_visit[cur]:
            continue

        is_visit[cur] = True
        cnt += 1
        max_time = max(max_time, cost)

        for i, j in ls:
            if not is_visit[i] and dis[i] > j + cost:
                dis[i] = j + cost
                heapq.heappush(q, (dis[i], i))

    print("{} {}".format(cnt, max_time))


    test_case -= 1