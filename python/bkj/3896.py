# https://www.acmicpc.net/problem/3986
import sys
def solution(s):
    good_word = s.strip()

    while 'AA' in good_word or 'BB' in good_word:
        if 'AA' in good_word:
            good_word = good_word.replace('AA', '')
        if 'BB' in good_word:
            good_word = good_word.replace('BB', '')

    if len(good_word) > 0 :
        return False

    return True

if __name__ == '__main__':
    testCase = int(sys.stdin.readline())
    cnt = 0

    while testCase > 0:
        testCase -= 1

        str = sys.stdin.readline()

        if(solution(str)):
            cnt += 1

    print(cnt)