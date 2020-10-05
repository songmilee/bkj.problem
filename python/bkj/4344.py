import sys


def solution(s):
    scores = list(map(int, s.split(" ")))
    size = scores[0]

    avg = sum(scores[1:]) / size
    filter_avg = len(list(filter(lambda x: x > avg, scores[1:])))

    result = filter_avg / float(size) * 100
    print("{0:.3f}%".format(result))


if __name__ == '__main__':
    input = sys.stdin.readline

    test_case = int(input())

    while test_case > 0:
        test_case -= 1

        solution(input())
