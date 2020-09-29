#https://www.acmicpc.net/problem/2675
import sys

def solution(r, s):
    result_str = []
    str_list = list(s)

    for i in str_list:
        result_str.append(i * r)

    result = ''.join(result_str)
    print(result)

if __name__ == '__main__':
    testCase = int(sys.stdin.readline())

    while testCase > 0:
        testCase -= 1

        r, s = sys.stdin.readline().split(" ")
        solution(int(r), s.strip())
