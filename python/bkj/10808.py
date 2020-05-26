# 10808
# 주어진 문자열 내에서 알파벳 갯수를 세는 문제

# 표준 입출력으로 문자열을 받음
s = input()

# 알파벳 크기를 만듦
size = ord('z') - ord('a') + 1

for i in range(size):
    value = chr(ord('a') + i)

    #count 함수를 통해 문자열 함수의 알파벳을 셀 수 있음
    print(s.count(value), end=' ')
