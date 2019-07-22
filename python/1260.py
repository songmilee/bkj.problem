import sys
import queue

def main():
    s = sys.stdin.readline().split(" ")
    vertex = int(s[0])
    s_vertex = int(s[2]) - 1
    graph = [[0] * vertex for _ in range(vertex) ]

    edge = int(s[1])

    for i in range(edge):
        temp = sys.stdin.readline().split(" ")
        x = int(temp[0]) - 1
        y = int(temp[1]) - 1

        graph[x][y] = 1
        graph[y][x] = 1

    dfs_visit = [False] * vertex

    dfs(vertex, graph, dfs_visit, s_vertex)
    print()
    bfs(vertex, graph, s_vertex)

def dfs(vertex, graph, isVisit, s_vertex):
    if isVisit[s_vertex]:
        return
    else:
        print(s_vertex + 1, end=' ')
        isVisit[s_vertex] = True

        for i in range(vertex):
            if not isVisit[i] and graph[s_vertex][i] == 1:
                dfs(vertex, graph, isVisit, i)


def bfs(vertex, graph, s_vertex):
    q = queue.Queue()

    q.put(s_vertex)

    isVisit = [False] * vertex

    while not q.empty():
        cur = q.get()
        print(cur + 1, end=' ')
        isVisit[cur] = True

        for i in range(vertex):
            if not isVisit[i] and graph[cur][i] == 1:
                isVisit[i] = True
                q.put(i)




if __name__ == "__main__":
    main()