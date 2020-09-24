import sys
def solution(n, k, multi):
    can_use_cnt = 0

    for i in multi:
        can_use_cnt += int((i + 1) / 2)
    
    if can_use_cnt >= n :
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    input = sys.stdin.readline

    n, k = input().split(" ")
    n = int(n)
    k = int(k)

    multitabs = [int(i) for i in input().split(" ")]

    print(solution(n, k, multitabs))