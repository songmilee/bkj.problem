# https://www.acmicpc.net/problem/4949
import sys
def solution(s):
    start_bracket = []
    answer = "yes"

    for i in s:
        if i != '(' and i != ')' and i !='[' and i !=']': continue

        if i == "(":
            start_bracket.append("(")
        elif i == "[":
            start_bracket.append("[")
        elif i == ")":
            if len(start_bracket) < 1:
                answer = "no"
                break
            elif start_bracket[-1] != "(":
                answer = "no"
                break
            start_bracket.pop()

        elif i == "]":
            if len(start_bracket) < 1:
                answer = "no"
                break
            elif start_bracket[-1] != "[":
                answer = "no"
                break
            start_bracket.pop()

    if len(start_bracket) > 0:
        answer = "no"

    return answer

if __name__ == "__main__":
    input = sys.stdin.readline

    while True:
        s = input()

        if s.rstrip() == ".": break

        print(solution(s))
