# https://www.acmicpc.net/problem/2869
import sys
import math

def solution(a, b, v):
    spend_days = math.ceil((v - b) / (a - b))

    return int(spend_days)

if __name__ == '__main__':
    input = sys.stdin.readline().split(" ")

    a = int(input[0])
    b = int(input[1])
    v = int(input[2])

    s = solution(a, b, v)

    print(s)