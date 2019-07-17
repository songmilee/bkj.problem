#총 테스트케이스를 받음
testCase = int(input())

# 갯수만큼 테스트케이스를 받음
while testCase > 0:
    s = input()

    # 문자열을 받어 공백으로 구분
    data = s.split(" ")
    size = len(data[0])

    print("Distances:", end=' ')

    for i in range(size):
        #ord를 이용해 숫자로 변환
        x_val = ord(data[0][i])
        y_val = ord(data[1][i])

        if y_val >= x_val:
            print(y_val - x_val, end=' ')
        else:
            print(y_val + 26 - x_val, end=' ')

    print()
    testCase = testCase - 1