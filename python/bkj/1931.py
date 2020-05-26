'''
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
---
4

9 
8 8
5 8
3 4
2 5 
2 7
8 8
1 10
3 3
10 10
---
6
'''
import sys

def main():
    N = int(sys.stdin.readline()) # 1 ~ 100000
    meeting = [list(map(int, sys.stdin.readline().strip().split(" "))) for _ in range(N)]
    meeting.sort(key=lambda x: [x[1], x[0]])

    end_time = 0
    cnt = 0
    for i in meeting:
        if end_time <= i[0]:
            end_time = i[1]
            cnt = cnt + 1
    
    print(meeting)
    print(cnt)

if __name__ == "__main__":
    main()