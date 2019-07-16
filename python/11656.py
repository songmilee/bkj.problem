
s = input()

size = len(s)
end_list = [0] * size # 빈 배열 선언

# 접미사 슬라이싱
for i in range(size):
    end_list[i] = s[i:size]

# 문자열 비교를 통해 사전 순 정렬
for i in range(size):
    for j in range(i+1, size):
        if end_list[i] > end_list[j]: # 문자열 비교
            tmp = end_list[i]
            end_list[i] = end_list[j]
            end_list[j] = tmp

# 결과 
for i in range(size):
    print(end_list[i])

