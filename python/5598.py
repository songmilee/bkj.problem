val = input() #string을 입력으로 받음

result = "" # 결과 보여줄 변수

# 최대, 최소 값
min_val = ord('A')
max_val = ord('Z')

#글자 수 만큼 돌면서 암호 해독
for i in range(len(val)):
    temp = ord(val[i]) - 3 # 값을 뒤로 보냄

    # A, B, C 처리
    if temp < min_val:
        temp = (temp + max_val) % 26 + min_val + 1

    result += chr(temp)

#결과 출력
print(result)