# p.6118, 다익스트라 알고리즘, heapq 사용법 잘 알기!

import sys
import heapq

MAX_VALUE = 999999

def main():
    N, M = map(int, sys.stdin.readline().split(' '))

    edge = [[] for i in range(N)]
    path = [MAX_VALUE] * N

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split(' '))

        if not(b-1 in edge[a-1]):
            edge[a-1].append(b-1)

        if not (a-1 in edge[b-1]):
            edge[b-1].append(a-1)

    findPath(edge, path)
    # print(path)
    max_len = max(path)
    max_cnt = path.count(max_len)
    max_vertex = path.index(max_len) + 1

    print(str(max_vertex)+" "+str(max_len)+" "+str(max_cnt))


def findPath(edge, path):
    q = []
    is_visit = [False] * len(edge)

    heapq.heappush(q, (0, 0))
    path[0] = 0

    while q:
        cost, cur = heapq.heappop(q)
        is_visit[cur] = True

        list = edge[cur]
        for i in range(len(list)):
            val = list[i]
            if not is_visit[val] and path[val] > cost + 1:
                path[val] = cost + 1
                heapq.heappush(q, (path[val], val))



if __name__ == "__main__":
    main()