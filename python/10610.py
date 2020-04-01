import sys

'''
문자열로 처리하는 것이 핵심
가능 문자열은 합의 규칙이 있음
가능 문자열을 받았을 때 큰 순서대로 소트
'''
def main():
    N = sys.stdin.readline().strip()

    result = -1
    sum_n = 0
    can_n = False

    val_list = []
    for i in N:
        if ord(i) - ord('0') == 0:
            can_n = True
        sum_n = sum_n + int(i)
        val_list.append(i)

    
    if not can_n or sum_n%3 != 0:
        print(-1)
    else:
        val_list.sort(reverse=True)
        for i in val_list:
            print(i, end='')
    

if __name__ == "__main__":
    main()