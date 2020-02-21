'''
3 3
1 2 2
3 1 3
2 3 2
1 3
'''
import sys
import queue

n = -1
land = []
start = -1
end = -1

def main():
    global n, land, start, end

    n, m = map(int, sys.stdin.readline().split(" "))
    land = [ [] for _ in range(n)]

    maxWeight = -1
    for _ in range(m):
        a, b, c = sys.stdin.readline().split(" ")
        land[int(a) - 1].append([int(b) - 1, int(c)])
        land[int(b) - 1].append([int(a) - 1, int(c)])
        maxWeight = max(maxWeight, int(c))


    s, e = map(int, sys.stdin.readline().split(" "))
    start = s - 1
    end = e - 1

    low = 0
    high = maxWeight

    while low <= high:
        mid = (low + high) / 2

        if bfs(mid):
            low = mid + 1
        else:
            high = mid - 1

    print(high)


def bfs(mid):
    global start, end, land, n
    q = queue.Queue()
    isVisit = [False] * n

    q.put(start)
    isVisit[start] = True

    while not q.empty():
        point = q.get()

        if point == end :
            return True

        for i in land[point]:
            next_point, next_weight = i

            if not isVisit[next_point] and mid <= next_weight:
                isVisit[next_point] = True
                q.put(next_point)

    return False

if __name__ == "__main__":
    main()